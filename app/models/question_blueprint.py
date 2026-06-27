from dataclasses import dataclass, field


@dataclass
class QuestionBlueprint:

    concept: str

    coverage: str

    priority: int

    mcq: int

    case_based: int

    hots: int

    assertion_reason: int

    subjective: int

    easy: int

    medium: int

    hard: int

    bloom_levels: list = field(default_factory=list)

    misconceptions: list = field(default_factory=list)

    applications: list = field(default_factory=list)