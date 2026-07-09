# 🤖 Autonomous AI Agent using FastAPI & Gemini

An autonomous AI agent capable of understanding natural language requests, creating an execution plan, executing tasks, reviewing its own output, and generating a professional Microsoft Word document.

---

## 🚀 Features

- FastAPI REST API
- Natural Language Request Processing
- Autonomous Planning
- Multi-Step Task Execution
- Reflection / Self Review
- Microsoft Word (.docx) Generation
- Input Validation & Guardrails
- Structured JSON Responses
- Modular Architecture

---

## 🏗 Architecture

```
                POST /agent
                      │
                      ▼
             Request Validation
                      │
                      ▼
              Autonomous Planner
                      │
                      ▼
               Task Executor
                      │
                      ▼
             Reflection Agent
                      │
                      ▼
        Microsoft Word Generator
                      │
                      ▼
              generated_docs/
```

---

## 📁 Project Structure

```
autonomous-ai-agent/
│
├── app.py
├── config.py
├── llm.py
├── models.py
├── planner.py
├── executor.py
├── reflection.py
├── validator.py
├── prompts.py
├── utils.py
├── document_generator.py
├── requirements.txt
├── .env.example
├── README.md
│
└── generated_docs/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
cd autonomous-ai-agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Start FastAPI

```bash
python -m uvicorn app:app --reload
```

---

## API Endpoint

### POST /agent

Request

```json
{
    "request":"Create a business proposal for an AI Hospital Assistant"
}
```

Response

```json
{
    "status":"success",
    "execution_plan":[...],
    "document_path":"generated_docs/Proposal.docx",
    "document_preview":"..."
}
```

---

## Engineering Improvement

Implemented **Request Validation & Guardrails**

Features:

- Empty input validation
- Minimum request length
- Maximum request length
- Prompt injection detection
- Structured error handling

---

## Technologies

- Python
- FastAPI
- Gemini API
- python-docx
- Pydantic
- dotenv

---

## Future Improvements

- Conversation Memory
- Tool Calling
- RAG Integration
- Database Storage
- Multi-Agent Collaboration
- Streaming Responses
- Authentication

---

## Author

Naveen