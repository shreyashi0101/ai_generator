from app.prompting.builder import PromptBuilder
from app.utils.json_parser import JSONParser
from app.agents.json_repair_agent import JSONRepairAgent


class QuestionGenerator:
    """
    Generates questions using the configured LLM.
    Automatically repairs malformed JSON if needed.
    """

    def __init__(self, llm):

        self.llm = llm

        self.builder = PromptBuilder()

        self.repair_agent = JSONRepairAgent()

    def generate(
        self,
        concept,
        task,
    ):

        prompt = self.builder.build_prompt(
            concept,
            task,
        )

        response = self.llm.generate(
            prompt
        )

        try:

            data = JSONParser.parse(
                response
            )

        except Exception:

            print(
                "Repairing malformed JSON..."
            )

            data = self.repair_agent.repair(
                response
            )

        if isinstance(
            data,
            dict,
        ):

            data = [data]

        if not isinstance(
            data,
            list,
        ):

            raise RuntimeError(
                "Question generation failed."
            )

        # -------------------------------------------------
        # Prototype Version
        # Skip quality evaluation to keep execution fast
        # and avoid extra LLM/API calls.
        # -------------------------------------------------

        for question in data:

            question["quality"] = {

                "overall": "Not Evaluated",

                "feedback": "Quality evaluation disabled in prototype."

            }

        return data