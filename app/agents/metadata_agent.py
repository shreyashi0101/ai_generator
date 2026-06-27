from app.agents.base_agent import BaseAgent
from app.utils.json_parser import JSONParser


class MetadataAgent(BaseAgent):

    PROMPT_FILE = "metadata_extraction.txt"

    def extract(self, chapter: str):

        response = self.run(
            chapter=chapter
        )

        print("\n===== METADATA RAW RESPONSE =====")
        print(response)
        print("=================================\n")

        data = JSONParser.parse(response)

        print(type(data))
        print(data)

        return data