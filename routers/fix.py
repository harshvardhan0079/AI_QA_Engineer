from fastapi import APIRouter

from models.schemas import FixRequest
from utils.gemini import ask_gemini

router = APIRouter()


@router.post("/fix-code")
def fix_code(request: FixRequest):

    prompt = f"""
You are an expert Python developer.

Fix the following Python code.

Rules:
1. Return ONLY corrected Python code.
2. Do not explain anything.
3. Preserve functionality unless it contains bugs.

Code:
{request.code}
"""

    try:
        fixed_code = ask_gemini(prompt)

        return {
            "fixed_code": fixed_code,
            "confidence": 95
        }

    except Exception as e:
        return {
            "error": str(e)
        }