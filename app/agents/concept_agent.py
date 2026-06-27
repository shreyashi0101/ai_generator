from app.agents.base_agent import BaseAgent
from app.utils.json_parser import JSONParser


class ConceptAgent(BaseAgent):

    PROMPT_FILE = "concept_extraction.txt"

    def extract(
        self,
        chapter: str,
    ):

        response = self.run(
            chapter=chapter
        )

        data = JSONParser.parse(
            response
        )

        # If the LLM returned a list,
        # wrap it into the expected format.
        if isinstance(data, list):

            return {
                "concepts": data
            }

        return data