from pathlib import Path

from app.agents.metadata_agent import MetadataAgent
from app.agents.concept_agent import ConceptAgent
from app.agents.enrichment_agent import EnrichmentAgent
from app.agents.misconception_agent import MisconceptionAgent
from app.agents.application_agent import ApplicationAgent
from app.agents.relationship_agent import RelationshipAgent
from app.agents.bloom_agent import BloomAgent

from app.pipeline.knowledge_merger import KnowledgeMerger


class PipelineOrchestrator:

    def __init__(
        self,
        debug=False,
    ):

        self.debug = debug

        self.metadata_agent = MetadataAgent()

        self.concept_agent = ConceptAgent()

        self.enrichment_agent = EnrichmentAgent()

        self.misconception_agent = MisconceptionAgent()

        self.application_agent = ApplicationAgent()

        self.relationship_agent = RelationshipAgent()

        self.bloom_agent = BloomAgent()

        self.merger = KnowledgeMerger()

    def build_knowledge(
        self,
        chapter_path: str,
    ):

        print("\nLoading chapter...")

        chapter = Path(
            chapter_path
        ).read_text(
            encoding="utf-8"
        )

        print("Extracting metadata...")

        metadata = self.metadata_agent.extract(
            chapter
        )
        print("\n===== METADATA DEBUG =====")
        print(type(metadata))
        print(metadata)
        print("==========================\n")

        print("Extracting concepts...")

        concepts = self.concept_agent.extract(
            chapter
        )

        concept_list = concepts["concepts"]

        if self.debug:

            print("\nDEBUG MODE ENABLED")

            concept_list = concept_list[:1]

        enrichments = []

        misconceptions = []

        applications = []

        relationships = []

        bloom_levels = []

        total = len(
            concept_list
        )

        for i, concept in enumerate(
            concept_list,
            start=1,
        ):

            print(
                f"\n[{i}/{total}] {concept['name']}"
            )

            # -------------------------
            # Enrichment
            # -------------------------

            enrichments.append(

                self.enrichment_agent.enrich(
                    concept,
                    chapter,
                )

            )

            # -------------------------
            # Misconceptions
            # -------------------------

            mis = self.misconception_agent.extract(
                concept,
                chapter,
            )

            if isinstance(
                mis,
                list,
            ):

                mis = {

                    "name": concept["name"],

                    "misconceptions": mis,

                }

            misconceptions.append(
                mis
            )

            # -------------------------
            # Applications
            # -------------------------

            app = self.application_agent.extract(
                concept,
                chapter,
            )

            if isinstance(
                app,
                list,
            ):

                app = {

                    "name": concept["name"],

                    "applications": app,

                }

            applications.append(
                app
            )

            # -------------------------
            # Relationships
            # -------------------------

            rel = self.relationship_agent.extract(
                concept,
                chapter,
            )

            if isinstance(
                rel,
                list,
            ):

                rel = {

                    "name": concept["name"],

                    "relationships": rel,

                }

            relationships.append(
                rel
            )

            # -------------------------
            # Bloom
            # -------------------------

            bloom = self.bloom_agent.extract(
                concept,
                chapter,
            )

            if isinstance(
                bloom,
                list,
            ):

                bloom = {

                    "name": concept["name"],

                    "bloom_levels": bloom,

                }

            bloom_levels.append(
                bloom
            )

        concepts["concepts"] = concept_list

        knowledge = self.merger.merge(

            metadata,

            concepts,

            enrichments,

            misconceptions,

            applications,

            relationships,

            bloom_levels,

        )

        self.merger.save(
            knowledge
        )

        print(
            "\nknowledge.json created successfully."
        )

        return knowledge