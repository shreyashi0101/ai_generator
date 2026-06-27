from app.agents.base_agent import BaseAgent
from app.utils.json_parser import JSONParser


class RelationshipAgent(BaseAgent):

    PROMPT_FILE = "relationship_extraction.txt"

    def extract(
        self,
        concept: dict,
        chapter: str,
    ):

        response = self.run(
            concept=concept["name"],
            chapter=chapter,
        )

        return JSONParser.parse(response)