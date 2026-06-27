from dataclasses import dataclass, field

from app.models.concept import Concept


@dataclass
class Knowledge:

    subject: str

    grade: str

    chapter: str

    concepts: list[Concept] = field(default_factory=list)