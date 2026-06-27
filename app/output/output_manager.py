from app.utils.save_json import save_json


class OutputManager:

    def save_knowledge(
        self,
        knowledge,
    ):

        save_json(
            knowledge,
            "output/knowledge.json",
        )

    def save_questions(
        self,
        questions,
    ):

        save_json(
            questions,
            "output/questions.json",
        )

    def save_plan(
        self,
        plan,
    ):

        save_json(
            plan,
            "output/question_plan.json",
        )