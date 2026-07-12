from fastapi import APIRouter

from models.schemas import TestRequest
from utils.gemini import ask_gemini

router = APIRouter()


@router.post("/generate-tests")
def generate_tests(request: TestRequest):

    prompt = f"""
You are a Senior Python QA Engineer.

Generate pytest test cases.

Requirements:
- Cover normal cases
- Cover edge cases
- Cover invalid inputs
- Return ONLY pytest code

Python Code:

{request.code}
"""

    try:

        tests = ask_gemini(prompt)

        return {
            "tests": tests
        }

    except Exception as e:

        return {
            "error": str(e)
        }