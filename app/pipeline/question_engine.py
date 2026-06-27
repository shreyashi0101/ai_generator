from app.planner.planner import QuestionPlanner
from app.planner.task_builder import TaskBuilder
from app.validator.question_validator import QuestionValidator
from app.validator.duplicate_remover import DuplicateRemover


class QuestionEngine:

    def __init__(self, generator):

        self.generator = generator

        self.planner = QuestionPlanner()

        self.task_builder = TaskBuilder()

        self.validator = QuestionValidator()

        self.duplicate = DuplicateRemover()

    def generate_question_bank(
        self,
        knowledge,
    ):

        questions = []

        for concept in knowledge["concepts"]:

            blueprint = self.planner.create_blueprint(
                concept
            )

            tasks = self.task_builder.build_tasks(
                blueprint
            )

            for task in tasks:

                generated = self.generator.generate(
                    concept,
                    task,
                )

                questions.extend(generated)

        questions = self.validator.validate(
            questions
        )

        questions = self.duplicate.remove(
            questions
        )

        return questions