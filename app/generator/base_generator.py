from app.prompting.builder import PromptBuilder


class BaseGenerator:

    def __init__(self, llm):

        self.llm = llm

        self.builder = PromptBuilder()