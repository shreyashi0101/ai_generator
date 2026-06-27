from app.pipeline.orchestrator import PipelineOrchestrator
from app.pipeline.question_engine import QuestionEngine

from app.generator.question_generator import QuestionGenerator
from app.llm.gemini_manager import GeminiManager

from app.output.output_manager import OutputManager


# =====================================
# DEBUG MODE
# =====================================

DEBUG = False

CHAPTER_PATH = (
    "input/test_chapter.txt"
    if DEBUG
    else "input/chapter.txt"
)


def main():

    print("=" * 70)
    print("AI Assessment Question Generation Engine")
    print("=" * 70)

    orchestrator = PipelineOrchestrator(
        debug=DEBUG
    )

    knowledge = orchestrator.build_knowledge(
        CHAPTER_PATH
    )

    output = OutputManager()

    output.save_knowledge(
        knowledge
    )

    llm = GeminiManager()

    generator = QuestionGenerator(
        llm
    )

    engine = QuestionEngine(
        generator
    )

    print("\nGenerating Question Bank...\n")

    questions = engine.generate_question_bank(
        knowledge
    )

    output.save_questions(
        questions
    )

    print("\n" + "=" * 70)
    print("Project Completed Successfully")
    print("=" * 70)

    print(
        f"\nGenerated {len(questions)} questions."
    )


if __name__ == "__main__":
    main()