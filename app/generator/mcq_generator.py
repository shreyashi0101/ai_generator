import json

from app.generator.base_generator import BaseGenerator


class MCQGenerator(BaseGenerator):

    def generate(
        self,
        concept,
        count,
        difficulty,
    ):

        prompt = self.builder.build_question_prompt(

            concept=concept,

            blueprint=count,

            question_type="Multiple Choice",

            difficulty=difficulty,
        )

        prompt += """

Generate questions in the following JSON format.

[
    {
        "question":"",

        "options":[
            "",
            "",
            "",
            ""
        ],

        "answer":"",

        "explanation":""
    }
]

Return ONLY JSON.
"""

        response = self.llm.generate(prompt)

        return json.loads(response)