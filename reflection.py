from llm import ask_llm
from prompts import REFLECTION_PROMPT


def reflect_document(document: str) -> str:
    """
    Reviews and improves the generated document.
    """

    prompt = REFLECTION_PROMPT.replace(
        "{document}",
        document
    )

    try:
        improved_document = ask_llm(prompt)

        return improved_document

    except Exception:

        # Fallback if reflection fails
        return document