import json
from pathlib import Path


class KnowledgeMerger:

    def merge(
        self,
        metadata,
        concepts,
        enrichments,
        misconceptions,
        applications,
        relationships,
        bloom_levels,
    ):

        knowledge = {}

        # Create an entry for every concept
        for concept in concepts["concepts"]:

            knowledge[concept["name"]] = {

                "id": concept["id"],

                "name": concept["name"],

                "summary": "",

                "definition": "",

                "keywords": [],

                "examples": [],

                "formulae": [],

                "facts": [],

                "learning_objectives": [],

                "misconceptions": [],

                "applications": [],

                "relationships": [],

                "bloom_levels": []
            }

        # -----------------------------
        # Enrichment
        # -----------------------------

        for item in enrichments:

            name = item["name"]

            if name not in knowledge:
                continue

            knowledge[name]["summary"] = item.get(
                "summary",
                "",
            )

            knowledge[name]["definition"] = item.get(
                "definition",
                "",
            )

            knowledge[name]["keywords"] = item.get(
                "keywords",
                [],
            )

            knowledge[name]["examples"] = item.get(
                "examples",
                [],
            )

            knowledge[name]["formulae"] = item.get(
                "formulae",
                [],
            )

            knowledge[name]["facts"] = item.get(
                "facts",
                [],
            )

            knowledge[name]["learning_objectives"] = item.get(
                "learning_objectives",
                [],
            )

        # -----------------------------
        # Misconceptions
        # -----------------------------

        for item in misconceptions:

            name = item["name"]

            if name in knowledge:

                knowledge[name]["misconceptions"] = item.get(
                    "misconceptions",
                    [],
                )

        # -----------------------------
        # Applications
        # -----------------------------

        for item in applications:

            name = item["name"]

            if name in knowledge:

                knowledge[name]["applications"] = item.get(
                    "applications",
                    [],
                )

        # -----------------------------
        # Relationships
        # -----------------------------

        for item in relationships:

            name = item["name"]

            if name in knowledge:

                knowledge[name]["relationships"] = item.get(
                    "relationships",
                    [],
                )

        # -----------------------------
        # Bloom Levels
        # -----------------------------

        for item in bloom_levels:

            name = item["name"]

            if name in knowledge:

                knowledge[name]["bloom_levels"] = item.get(
                    "bloom_levels",
                    [],
                )

        # -----------------------------
        # Final Knowledge Object
        # -----------------------------

        final = {

            "subject": metadata.get(
                "subject",
                "",
            ),

            "grade": metadata.get(
                "grade",
                "",
            ),

            "chapter": metadata.get(
                "chapter",
                "",
            ),

            "summary": metadata.get(
                "summary",
                "",
            ),

            "learning_outcomes": metadata.get(
                "learning_outcomes",
                [],
            ),

            "concepts": list(
                knowledge.values()
            )

        }

        return final

    def save(
        self,
        knowledge,
        path="output/knowledge.json",
    ):

        Path("output").mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                knowledge,
                f,
                indent=4,
                ensure_ascii=False,
            )

        print(f"\nKnowledge saved to {path}")