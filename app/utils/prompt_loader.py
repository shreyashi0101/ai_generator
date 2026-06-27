from pathlib import Path


class PromptLoader:
    """
    Loads prompt templates from the prompts directory.
    """

    def __init__(self):
        self.prompt_dir = Path("prompts")

    def load(self, filename: str) -> str:

        path = self.prompt_dir / filename

        if not path.exists():
            raise FileNotFoundError(
                f"Prompt '{filename}' not found."
            )

        return path.read_text(encoding="utf-8")


# Singleton instance
_loader = PromptLoader()


def load_prompt(filename: str) -> str:
    return _loader.load(filename)