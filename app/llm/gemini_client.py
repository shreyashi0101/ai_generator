import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class GeminiClient:
    """
    Azure AI Foundry / OpenAI wrapper.
    The class name is kept the same so the rest of the project
    does not need any import changes.
    """

    def __init__(self, api_key=None):

        self.client = OpenAI(

            base_url=os.getenv("AZURE_ENDPOINT"),

            api_key=api_key or os.getenv("AZURE_API_KEY"),
        )

        self.model = os.getenv("AZURE_MODEL")

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            temperature=0.2,
        )

        return response.choices[0].message.content.strip()