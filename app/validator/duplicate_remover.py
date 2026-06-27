class DuplicateRemover:

    def remove(self, questions):

        seen = set()

        unique = []

        for question in questions:

            q = question["question"].strip().lower()

            if q in seen:
                continue

            seen.add(q)

            unique.append(question)

        return unique