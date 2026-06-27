from app.agents.base_agent import BaseAgent
from app.utils.json_parser import JSONParser


class JSONRepairAgent(BaseAgent):

    PROMPT_FILE = "json_repair.txt"

    def repair(
        self,
        broken_json: str,
    ):

        response = self.run(
            broken_json=broken_json
        )

        return JSONParser.parse(
            response
        )