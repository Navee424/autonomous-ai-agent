from llm import ask_llm
from prompts import PLANNER_PROMPT
from utils import extract_json


def create_execution_plan(user_request: str):
    """
    Creates an execution plan for the user request.
    """

    prompt = PLANNER_PROMPT.replace(
        "{request}",
        user_request
    )

    response = ask_llm(prompt)

    plan = extract_json(response)

    tasks = []

    for index, task in enumerate(plan["tasks"], start=1):

        tasks.append({

            "id": index,

            "task": task,

            "status": "pending"

        })

    return tasks