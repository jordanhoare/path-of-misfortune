import json
import logging
from typing import Any

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format="%(message)s")

POEDB_URL = "https://poedb.tw/us/Ascendancy_class"


def fetch_page(url: str) -> BeautifulSoup | None:
    """Fetches the webpage and returns a BeautifulSoup object."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None
    return BeautifulSoup(response.text, "html.parser")


def extract_class_info(row: BeautifulSoup) -> list[dict[str, Any]]:
    """Extracts class information from a table row."""
    class_info = []
    character_class_anchor = row.find("td").find("a") if row.find("td") else None  # type: ignore[union-attr]
    character_class = (
        character_class_anchor["class"][0] if character_class_anchor else None  # type: ignore[index]
    )
    if character_class:
        ascendancy_anchors = (
            row.find_all("td")[1].find_all("a") if len(row.find_all("td")) > 1 else []
        )
        for ascendancy_anchor in ascendancy_anchors:
            ascendancy_name = (
                ascendancy_anchor["class"][0] if ascendancy_anchor else None
            )
            img_tag = ascendancy_anchor.find("img")
            image_url = img_tag["src"] if img_tag else None
            if ascendancy_name and image_url:
                class_info.append(
                    {
                        "ascendancy": ascendancy_name,
                        "character": character_class,
                        "image_url": image_url,
                    }
                )
    return class_info


def scrape_classes(url: str) -> list[dict[str, Any]]:
    soup = fetch_page(url)
    if soup is None:
        logging.error("Failed to fetch page content.")
        return []

    ascendancy_section = soup.find("div", id="AscendancyClasses")
    if ascendancy_section:
        tbody = ascendancy_section.find("tbody")
        if tbody:
            rows = tbody.find_all("tr")  # type: ignore[union-attr]
            all_classes = []
            for row in rows:
                class_info = extract_class_info(row)
                all_classes.extend(class_info)
            return all_classes
    return []


def save_to_json(data: list[dict[str, Any]], path: str) -> None:
    """Saves the scraped data to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main() -> None:
    classes = scrape_classes(POEDB_URL)
    save_to_json(classes, "app/data/classes.json")
    logging.info(f"Scraped and saved {len(classes)} classes/ascendancies.")


if __name__ == "__main__":
    main()
