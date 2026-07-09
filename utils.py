import json
import re


def extract_json(response: str) -> dict:
    """
    Extracts JSON from Gemini response.
    """

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    match = re.search(
        r"\{.*\}",
        response,
        re.DOTALL
    )

    if not match:
        raise ValueError(
            "Planner returned invalid JSON."
        )

    return json.loads(match.group())


def clean_text(text: str) -> str:
    """
    Removes unnecessary whitespace.
    """

    return "\n".join(
        line.strip()
        for line in text.splitlines()
        if line.strip()
    )