from dataclasses import dataclass, field


@dataclass
class Question:

    id: int

    concept: str

    question_type: str

    difficulty: str

    bloom_level: str

    question: str

    options: list = field(default_factory=list)

    answer: str = ""

    explanation: str = ""

    source_concepts: list = field(default_factory=list)

    target_misconceptions: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)