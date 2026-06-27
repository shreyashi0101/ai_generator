from app.llm.gemini_client import GeminiClient


class GeminiManager:

    def __init__(self):

        self.client = GeminiClient()

    def generate(
        self,
        prompt: str,
    ) -> str:

        return self.client.generate(prompt)