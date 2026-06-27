from abc import ABC
from typing import Any

from app.llm.gemini_manager import GeminiManager
from app.utils.prompt_loader import load_prompt


class BaseAgent(ABC):
    """
    Base class for all AI agents.

    Responsibilities:
    - Load prompt template
    - Replace template variables
    - Send prompt to the configured LLM
    """

    PROMPT_FILE = ""

    def __init__(self):
        self.llm = GeminiManager()

    def build_prompt(self, variables: dict[str, Any]) -> str:
        """
        Load prompt template and replace placeholders.

        Example:
            {{chapter}}
            {{concept}}
        """

        prompt = load_prompt(self.PROMPT_FILE)

        for key, value in variables.items():

            prompt = prompt.replace(
                "{{" + key + "}}",
                str(value),
            )

        return prompt

    def run(self, **variables) -> str:
        """
        Build prompt and execute LLM call.
        """

        prompt = self.build_prompt(variables)

        return self.llm.generate(prompt)