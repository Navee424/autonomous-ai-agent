from pydantic import BaseModel, Field
from typing import List


class AgentRequest(BaseModel):
    request: str = Field(
        ...,
        description="Natural language request for the autonomous AI agent.",
        examples=["Create a business proposal for an AI-powered Hospital Assistant."]
    )


class Task(BaseModel):
    id: int
    task: str
    status: str
    result: str | None = None


class AgentResponse(BaseModel):
    status: str
    execution_plan: List[Task]
    document_path: str
    document_preview: str