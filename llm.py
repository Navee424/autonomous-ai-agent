import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to Gemini and returns the response.
    """

    try:
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        raise RuntimeError(
            f"Gemini API Error: {e}"
        )