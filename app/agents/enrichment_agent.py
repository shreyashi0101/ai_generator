from app.agents.base_agent import BaseAgent
from app.utils.json_parser import JSONParser


class EnrichmentAgent(BaseAgent):

    PROMPT_FILE = "concept_enrichment.txt"

    def enrich(self, concept: dict, chapter: str):

        response = self.run(
            concept=concept["name"],
            chapter=chapter,
        )

        data = JSONParser.parse(response)

        data["id"] = concept["id"]

        return data