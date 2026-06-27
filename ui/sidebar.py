import streamlit as st


def render_sidebar():

    st.sidebar.title("⚙ Controls")

    uploaded_file = st.sidebar.file_uploader(
        "Upload Chapter (.txt)",
        type=["txt"],
    )

    debug = st.sidebar.checkbox(
        "Debug Mode",
        value=True,
    )

    generate_knowledge = st.sidebar.button(
        "Generate Knowledge"
    )

    generate_questions = st.sidebar.button(
        "Generate Questions"
    )

    return {

        "uploaded_file": uploaded_file,

        "debug": debug,

        "generate_knowledge": generate_knowledge,

        "generate_questions": generate_questions,

    }