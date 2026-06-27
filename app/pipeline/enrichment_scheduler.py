from concurrent.futures import ThreadPoolExecutor

from app.agents.enrichment_agent import EnrichmentAgent


class EnrichmentScheduler:

    def __init__(self):

        self.agent = EnrichmentAgent()

    def enrich_all(
        self,
        concepts,
        chapter,
    ):

        with ThreadPoolExecutor(
            max_workers=3
        ) as executor:

            futures = [

                executor.submit(
                    self.agent.enrich,
                    concept["name"],
                    chapter,
                )

                for concept in concepts

            ]

            return [

                future.result()

                for future in futures

            ]