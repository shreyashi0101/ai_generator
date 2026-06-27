from app.models.question_blueprint import QuestionBlueprint


class QuestionPlanner:

    def create_blueprint(self, concept):

        misconceptions = len(
            concept.get("misconceptions", [])
        )

        applications = len(
            concept.get("applications", [])
        )

        relationships = len(
            concept.get("relationships", [])
        )

        priority = (
            misconceptions
            + applications
            + relationships
        )

        return QuestionBlueprint(

            concept=concept["name"],

            coverage="High",

            priority=priority,

            mcq=3,

            case_based=2 if applications else 1,

            hots=2 if relationships else 1,

            assertion_reason=2 if misconceptions else 1,

            subjective=3,

            easy=3,

            medium=5,

            hard=3,

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