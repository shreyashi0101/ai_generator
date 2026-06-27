import json
from pathlib import Path
import streamlit as st

from app.pipeline.orchestrator import PipelineOrchestrator
from app.pipeline.question_engine import QuestionEngine
from app.generator.question_generator import QuestionGenerator
from app.llm.gemini_manager import GeminiManager

st.set_page_config(
    page_title="AI Assessment Engine",
    page_icon="📚",
    layout="wide",
)

st.title("📚 AI Assessment Generation Engine")
st.caption("Mechanism Prototype for Intelligent NCERT Assessment Generation")

st.divider()

debug = st.checkbox(
    "🛠 Debug Mode",
    value=True,
    help="Uses input/test_chapter.txt instead of input/chapter.txt"
)

source = st.radio(
    "Choose Chapter Source",
    ["Existing Notes", "Upload Notes"]
)

chapter_path = None

if source == "Existing Notes":

    subject = st.selectbox(
        "Subject",
        ["Science"]
    )

    grade = st.selectbox(
        "Grade",
        ["6"]
    )

    chapter = st.selectbox(
        "Chapter",
        ["Materials Around Us"]
    )

    if debug:
        chapter_path = "input/test_chapter.txt"
        st.info("Using input/test_chapter.txt")
    else:
        chapter_path = "input/chapter.txt"
        st.info("Using input/chapter.txt")

else:

    uploaded = st.file_uploader(
        "Upload Notes (.txt)",
        type=["txt"]
    )

    if uploaded:
        Path("input").mkdir(exist_ok=True)

        chapter_path = "input/uploaded_notes.txt"

        with open(chapter_path, "wb") as f:
            f.write(uploaded.getbuffer())

        st.success("Uploaded successfully.")

st.divider()

if st.button(
    "🚀 Generate Assessment",
    use_container_width=True,
):

    if chapter_path is None:
        st.error("Please choose or upload a chapter.")
        st.stop()

    progress = st.progress(0)
    status = st.empty()

    try:

        status.write("Loading chapter...")
        progress.progress(10)

        orchestrator = PipelineOrchestrator(
            debug=debug
        )

        knowledge = orchestrator.build_knowledge(
            chapter_path
        )

        progress.progress(60)

        status.write("Generating Questions...")

        llm = GeminiManager()

        generator = QuestionGenerator(llm)

        engine = QuestionEngine(generator)

        questions = engine.generate_question_bank(
            knowledge
        )

        progress.progress(100)

        status.success("Assessment Generated Successfully!")

        st.divider()

        st.header("📖 Chapter Information")
        col1, col2 = st.columns(2)
        with col1:
         st.write(
        "**Subject:**",
        knowledge.get("subject", "-")
    )

        st.write(
        "**Grade:**",
        knowledge.get("grade", "-")
    )
        with col2:
         st.write(
        "**Chapter:**",
        knowledge.get("chapter", "-")
    )
        st.write("### Summary")
        st.write(
        knowledge.get(
        "summary",
        ""
    )       )
        if knowledge.get("learning_outcomes"):

         st.write("### Learning Outcomes")

        for outcome in knowledge["learning_outcomes"]:

         st.write("•", outcome)

        st.divider()

        st.header("🧠 Concepts")

        for concept in knowledge["concepts"]:

            with st.expander(concept["name"]):

                st.write("**Definition**")
                st.write(concept.get("definition", ""))

                st.write("**Summary**")
                st.write(concept.get("summary", ""))

                if concept.get("keywords"):
                    st.write("**Keywords**")
                    st.write(", ".join(concept["keywords"]))

                if concept.get("misconceptions"):
                    st.write("**Misconceptions**")
                    for m in concept["misconceptions"]:
                        st.write("•", m)

                if concept.get("applications"):
                    st.write("**Applications**")
                    for a in concept["applications"]:
                        st.write("•", a)

        st.divider()

        st.header("📝 Question Preview")

        preview = min(5, len(questions))

        for question in questions[:preview]:

            with st.expander(question["question"]):

                if question.get("options"):

                    for option in question["options"]:
                        st.write("•", option)

                st.success("Answer: " + question.get("answer", ""))

                st.info(question.get("explanation", ""))

                quality = question.get("quality")

                if quality:
                    st.write(
                        "**Quality Score:**",
                        quality.get("overall", "-")
                    )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                "⬇ Download Knowledge JSON",
                json.dumps(
                    knowledge,
                    indent=4,
                    ensure_ascii=False,
                ),
                file_name="knowledge.json",
                mime="application/json",
            )

        with col2:
            st.download_button(
                "⬇ Download Questions JSON",
                json.dumps(
                    questions,
                    indent=4,
                    ensure_ascii=False,
                ),
                file_name="questions.json",
                mime="application/json",
            )

    except Exception as e:

            st.error(f"Error: {e}")
