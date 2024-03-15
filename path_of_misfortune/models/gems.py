import json
from dataclasses import dataclass, field


@dataclass
class SkillGem:
    name: str
    link: str
    image_url: str | None = None
    tags: list[str] = field(default_factory=list)

    @classmethod
    def from_json(
        cls, json_file_path: str = "path_of_misfortune/data/skill_gems.json"
    ) -> list["SkillGem"]:
        with open(json_file_path, encoding="utf-8") as f:
            data = json.load(f)
        return [cls(**gem_data) for gem_data in data]
