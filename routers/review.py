from fastapi import APIRouter

from models.schemas import ReviewRequest
from utils.gemini import ask_gemini

router = APIRouter()


@router.post("/review")
def review_code(request: ReviewRequest):

    prompt = f"""
You are a Senior Python QA Engineer.

Review the following Python code.

Provide:

1. Bugs
2. Security Issues
3. Performance Improvements
4. Code Smells
5. Best Practices
6. Quality Score out of 10

Code:

{request.code}
"""

    try:
        review = ask_gemini(prompt)

        return {
            "review": review
        }

    except Exception as e:
        return {
            "error": str(e)
        }