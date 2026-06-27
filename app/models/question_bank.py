from dataclasses import dataclass, field

from app.models.question import Question


@dataclass
class QuestionBank:

    metadata: dict

    questions: list[Question] = field(default_factory=list)