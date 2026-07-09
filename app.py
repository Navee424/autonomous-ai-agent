from fastapi import FastAPI
from fastapi.responses import JSONResponse

from models import AgentRequest
from validator import validate_request

from planner import create_execution_plan
from executor import execute_tasks
from reflection import reflect_document
from document_generator import generate_word_document

app = FastAPI(
    title="Autonomous AI Agent",
    description="Autonomous AI Agent using FastAPI and Gemini",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "Autonomous AI Agent is running."
    }


@app.post("/agent")
def run_agent(request: AgentRequest):

    try:

        # Step 1
        validate_request(request.request)

        # Step 2
        execution_plan = create_execution_plan(
            request.request
        )

        # Step 3
        execution_result = execute_tasks(
            execution_plan,
            request.request
        )

        # Step 4
        improved_document = reflect_document(
            execution_result["document"]
        )

        # Step 5
        title = request.request[:40]

        document_path = generate_word_document(
            improved_document,
            title
        )

        # Final Response
        return JSONResponse(

            status_code=200,

            content={

                "status": "success",

                "execution_plan": execution_result["tasks"],

                "document_path": document_path,

                "document_preview": improved_document[:1000]

            }

        )

    except Exception as e:

        return JSONResponse(

            status_code=500,

            content={

                "status": "failed",

                "message": str(e)

            }

        )