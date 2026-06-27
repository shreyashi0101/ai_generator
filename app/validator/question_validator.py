class QuestionValidator:

    def validate(self, questions):

        valid = []

        required = [
            "question",
            "answer",
            "explanation",
        ]

        for question in questions:

            if not isinstance(question, dict):
                continue

            ok = True

            for field in required:

                if not question.get(field):

                    ok = False

                    break

            if ok:

                valid.append(question)

        return valid