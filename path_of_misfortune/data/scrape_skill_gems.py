import json
import logging
from typing import Any

import requests
from bs4 import BeautifulSoup, Tag

logging.basicConfig(level=logging.INFO, format="%(message)s")

POEDB_URL = "https://poedb.tw/us/Skill_Gems"


def fetch_page(url: str) -> BeautifulSoup | None:
    """Fetches the webpage and returns a BeautifulSoup object."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None
    return BeautifulSoup(response.text, "html.parser")


def extract_gem_info(row: Tag) -> dict[str, Any] | None:
    img_tag = row.find("img")
    gem_name_tags = row.find_all("td")
    if len(gem_name_tags) > 1 and isinstance(gem_name_tags[1], Tag):
        gem_name_tag = gem_name_tags[1].find("a")
        if gem_name_tag and isinstance(gem_name_tag, Tag):
            gem_link = f"https://poedb.tw{gem_name_tag.get('href', '')}"

            gem_name = gem_name_tag.get_text(strip=True)
            gem_image_url = (
                img_tag["src"] if img_tag and isinstance(img_tag, Tag) else None
            )
            tags_str = row.get(
                "data-tags", ""
            )  # This should not cause an error as it's correct usage
            gem_tags = tags_str.split() if isinstance(tags_str, str) else []

            return {
                "name": gem_name,
                "link": gem_link,
                "image_url": gem_image_url,
                "tags": gem_tags,
            }
    logging.warning(
        "Missing gem name or link for row: likely incorrect HTML structure."
    )
    return None


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
    save_to_json(gems_data, "path_of_misfortune/data/skill_gems.json")
    logging.info(f"Scraped and saved {len(gems_data)} skill gems.")


if __name__ == "__main__":
    main()
