from app.llm.gemini_manager import GeminiManager

llm = GeminiManager()

response = llm.generate("tell your model name ")

print(response)