from fastapi import APIRouter

from models.schemas import ExplainRequest
from utils.gemini import ask_gemini

router = APIRouter()


@router.post("/explain-code")
def explain_code(request: ExplainRequest):

    prompt = f"""
You are an expert Python instructor.

Explain the following Python code in simple English.

Include:
1. Overall purpose
2. Line-by-line explanation
3. Time Complexity
4. Space Complexity
5. Possible Improvements

Code:
{request.code}
"""

    try:

        explanation = ask_gemini(prompt)

        return {
            "explanation": explanation
        }

    except Exception as e:

        return {
            "error": str(e)
        }