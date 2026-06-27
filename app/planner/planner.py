from app.models.question_blueprint import QuestionBlueprint


class QuestionPlanner:
    """
    Creates a QuestionBlueprint for each concept.
    """

    def calculate_priority(self, concept) -> int:

        score = 10

        score += len(
            concept.get("misconceptions", [])
        ) * 3

        score += len(
            concept.get("relationships", [])
        ) * 2

        score += len(
            concept.get("applications", [])
        ) * 2

        score += len(
            concept.get("bloom_levels", [])
        ) * 2

        score += len(
            concept.get("keywords", [])
        )

        return score

    def create_blueprint(self, concept):

        priority = self.calculate_priority(
            concept
        )

        # ---------- MCQ ----------

        if priority >= 45:
            mcq = 6
        elif priority >= 30:
            mcq = 5
        else:
            mcq = 3

        # ---------- Case ----------

        case_based = min(
            3,
            max(
                1,
                len(
                    concept.get(
                        "applications",
                        [],
                    )
                ) // 3,
            ),
        )

        # ---------- HOTS ----------

        hots = min(
            3,
            max(
                1,
                len(
                    concept.get(
                        "relationships",
                        [],
                    )
                ) // 2,
            ),
        )

        # ---------- Assertion Reason ----------

        assertion_reason = min(
            3,
            max(
                1,
                len(
                    concept.get(
                        "misconceptions",
                        [],
                    )
                ) // 3,
            ),
        )

        # ---------- Subjective ----------

        if priority >= 40:
            subjective = 4
        elif priority >= 25:
            subjective = 3
        else:
            subjective = 2

        return QuestionBlueprint(

            concept=concept["name"],

            coverage="High",

            priority=priority,

            mcq=mcq,

            case_based=case_based,

            hots=hots,

            assertion_reason=assertion_reason,

            subjective=subjective,

            easy=30,

            medium=50,

            hard=20,

            bloom_levels=concept.get(
                "bloom_levels",
                [],
            ),

            misconceptions=concept.get(
                "misconceptions",
                [],
            ),

            applications=concept.get(
                "applications",
                [],
            ),
        )