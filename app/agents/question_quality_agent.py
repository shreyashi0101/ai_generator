from app.agents.base_agent import BaseAgent
from app.utils.json_parser import JSONParser


class QuestionQualityAgent(BaseAgent):

    PROMPT_FILE = "question_quality.txt"

    def evaluate(
        self,
        question_json: str,
        concept: str,
    ):

        response = self.run(

            question=question_json,

            concept=concept,

        )

        return JSONParser.parse(
            response
        )