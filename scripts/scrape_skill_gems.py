import json
import logging
import re
from typing import Any

import requests
from bs4 import BeautifulSoup, Tag

logging.basicConfig(level=logging.INFO, format="%(message)s")

POEDB_URL = "https://poedb.tw/us/Skill_Gems"


def fetch_page(url: str) -> BeautifulSoup | None:
    """Fetches the webpage and returns a BeautifulSoup object."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None
    return BeautifulSoup(response.text, "html.parser")


def extract_gem_info(row: Tag) -> dict[str, Any] | None:

    data_hover_tag = row.find("a", attrs={"data-hover": True})
    if not data_hover_tag or not isinstance(data_hover_tag, Tag):
        return None

    data_hover_value = data_hover_tag.get("data-hover", "")
    alternate_quality: bool = data_hover_value[-4:] in ["AltX", "AltY", "AltZ"]  # type: ignore[index, operator]

    gem_tags = row.find("div", class_="gem_tags small")
    if not gem_tags or not isinstance(gem_tags, Tag):
        return None

    gem_name_tag = gem_tags.find_previous_sibling("a")
    if not gem_name_tag or not isinstance(gem_name_tag, Tag):
        return None

    gem_name = gem_name_tag.get_text(strip=True)
    vaal: bool = gem_name.startswith("Vaal")

    gem_level_text = gem_name_tag.nextSibling
    gem_level_matches = re.findall(r"\d+", str(gem_level_text))
    gem_level = int(gem_level_matches[0]) if gem_level_matches else None

    img_tag = row.find("img")
    image_url = img_tag["src"] if img_tag and isinstance(img_tag, Tag) else ""

    return {
        "name": gem_name,
        "vaal": vaal,
        "level": gem_level,
        "link": f"https://poedb.tw{gem_name_tag.get('href', '')}",
        "image_url": image_url,
        "tags": [tag.strip() for tag in gem_tags.get_text(", ").split(",")],
        "alternative_quality": alternate_quality,
    }


def scrape_skill_gems(url: str) -> list[dict[str, Any]]:
    """Scrapes skill gem data from the given URL."""
    soup = fetch_page(url)
    if not soup:
        return []

    gems_data: list[dict[str, Any]] = []
    gems_section = soup.find_all("div", class_="clearfix row no-gutters")
    for section in gems_section:
        for table in section.find_all("table"):
            tbody = table.find("tbody")
            if tbody:
                for row in tbody.find_all("tr"):
                    gem_info = extract_gem_info(row)
                    if gem_info:
                        gems_data.append(gem_info)
                    else:
                        logging.warning("A gem entry was skipped due to missing data.")
    return gems_data


def save_to_json(data: list[dict[str, Any]], path: str) -> None:
    """Saves the scraped data to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main() -> None:
    gems_data = scrape_skill_gems(POEDB_URL)
    save_to_json(gems_data, "app/data/skill_gems.json")
    logging.info(f"Scraped and saved {len(gems_data)} skill gems.")


if __name__ == "__main__":
    main()
