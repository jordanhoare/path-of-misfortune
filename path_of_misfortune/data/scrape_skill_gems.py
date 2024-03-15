import json
import logging

import requests
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

POEDB_URL = "https://poedb.tw/us/Skill_Gems"

response = requests.get(POEDB_URL)

soup = BeautifulSoup(response.text, "html.parser")
gems_section = soup.find_all("div", class_="clearfix row no-gutters")

gems_data = []
for section in gems_section:
    for table in section.find_all("table"):
        tbody = table.find("tbody")
        if tbody:
            for row in tbody.find_all("tr"):
                img_tag = row.find("img")
                gem_name_tags = row.find_all("td")
                gem_name_tag = (
                    gem_name_tags[1].find("a") if len(gem_name_tags) > 1 else None
                )

                gem_link = (
                    "https://poedb.tw" + gem_name_tag["href"]
                    if gem_name_tag and gem_name_tag.has_attr("href")
                    else None
                )

                if gem_name_tag and gem_name_tag.get_text(strip=True):
                    gem_name = gem_name_tag.get_text(strip=True)
                    gem_image_url = img_tag["src"] if img_tag else None
                    gem_tags = row.get("data-tags", "").split()

                    gem_info = {
                        "name": gem_name,
                        "link": gem_link,
                        "image_url": gem_image_url,
                        "tags": gem_tags,
                    }
                    gems_data.append(gem_info)
                else:
                    # Include the URL in the warning if possible
                    if gem_link:
                        logging.warning(
                            f"A gem entry was skipped because the name could not be found. URL: {gem_link}"
                        )
                    else:
                        logging.warning(
                            "A gem entry was skipped because both the name and URL could not be found."
                        )
                    continue

# Saving to JSON
with open("path_of_misfortune/data/skill_gems.json", "w", encoding="utf-8") as f:
    json.dump(gems_data, f, ensure_ascii=False, indent=4)

logging.info(f"Scraped and saved {len(gems_data)} skill gems.")
