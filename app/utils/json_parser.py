import json


class JSONParser:
    """
    Robust parser for Gemini/Azure responses.
    """

    @staticmethod
    def parse(response: str):

        if response is None:
            raise ValueError("Model returned None.")

        text = response.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        # First try parsing the whole response
        try:
            return json.loads(text)
        except Exception:
            pass

        # If the model added extra text, extract the outermost JSON object
        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(text[start:end + 1])
            except Exception:
                pass

        # Otherwise extract the outermost JSON array
        start = text.find("[")
        end = text.rfind("]")

        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(text[start:end + 1])
            except Exception:
                pass

        raise ValueError(
            f"Could not parse JSON.\n\n{text}"
        )