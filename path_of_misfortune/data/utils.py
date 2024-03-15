import json

from path_of_misfortune.models.SkillGem import SkillGem


def load_skill_gems_from_json(json_file_path: str) -> list[SkillGem]:
    with open(json_file_path, encoding="utf-8") as f:
        data = json.load(f)

    skill_gems = [SkillGem(**gem_data) for gem_data in data]
    return skill_gems
