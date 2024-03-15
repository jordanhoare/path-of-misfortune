from dataclasses import dataclass, field


@dataclass
class SkillGem:
    name: str
    link: str
    image_url: str | None = None
    tags: list[str] = field(default_factory=list)
