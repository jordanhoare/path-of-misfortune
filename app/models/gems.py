import json
from dataclasses import dataclass, field


@dataclass
class SkillGem:
    name: str
    level: int
    link: str
    image_url: str | None = None
    tags: list[str] = field(default_factory=list)
    alternative_quality: bool = False
    vaal: bool = False

    @classmethod
    def from_json(
        cls, json_file_path: str = "app/data/skill_gems.json"
    ) -> list["SkillGem"]:
        with open(json_file_path, encoding="utf-8") as f:
            data = json.load(f)
        return [cls(**gem_data) for gem_data in data]
