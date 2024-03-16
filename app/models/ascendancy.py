import json
from dataclasses import dataclass


@dataclass
class Ascendancy:
    ascendancy: str
    character: str
    image_url: str | None = None

    @classmethod
    def from_json(
        cls, json_file_path: str = "app/data/classes.json"
    ) -> list["Ascendancy"]:
        with open(json_file_path, encoding="utf-8") as f:
            data = json.load(f)
        return [cls(**gem_data) for gem_data in data]
