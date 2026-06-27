class TaskBuilder:
    """
    Converts a QuestionBlueprint into executable generation tasks.
    """

    def build_tasks(self, blueprint):

        tasks = []

        def add(question_type, count):

            if count <= 0:
                return

            easy = max(1, int(count * 0.3))
            medium = max(1, int(count * 0.5))
            hard = max(0, count - easy - medium)

            if easy:
                tasks.append({
                    "type": question_type,
                    "difficulty": "Easy",
                    "count": easy
                })

            if medium:
                tasks.append({
                    "type": question_type,
                    "difficulty": "Medium",
                    "count": medium
                })

            if hard:
                tasks.append({
                    "type": question_type,
                    "difficulty": "Hard",
                    "count": hard
                })

        add("MCQ", blueprint.mcq)
        add("CaseBased", blueprint.case_based)
        add("HOTS", blueprint.hots)
        add("AssertionReason", blueprint.assertion_reason)
        add("Subjective", blueprint.subjective)

        return tasks