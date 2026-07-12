from fastapi import APIRouter

from utils.gemini import ask_gemini
from models.schemas import BugRequest

router = APIRouter()

@router.post("/find-bugs")
def find_bugs(request: BugRequest):

    prompt = f"""
You are a Senior Python QA Engineer.

Analyze the following Python code.

Find:

1. Bugs
2. Runtime Errors
3. Logical Errors
4. Security Issues
5. Best Practices

Return the answer in bullet points.

Code:
{request.code}
"""

    bugs = ask_gemini(prompt)

    return {
        "bugs": bugs
    }