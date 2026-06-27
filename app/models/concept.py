from dataclasses import dataclass, field


@dataclass
class Concept:

    id: int

    name: str

    summary: str = ""

    definition: str = ""

    keywords: list = field(default_factory=list)

    formulae: list = field(default_factory=list)

    examples: list = field(default_factory=list)

    learning_objectives: list = field(default_factory=list)

    misconceptions: list = field(default_factory=list)

    applications: list = field(default_factory=list)

    relationships: list = field(default_factory=list)

    bloom_levels: list = field(default_factory=list)