from fastapi import APIRouter
from models.schemas import Prompt
from utils.gemini import ask_gemini
import re

router = APIRouter()


@router.post("/scan-bugs")
def scan_bugs(request: Prompt):

    prompt = f"""
Analyze this Python code.

Count all bugs.

Classify into:

Critical
Medium
Minor

Return ONLY this format.

Critical: X
Medium: X
Minor: X

Python Code:

{request.prompt}
"""

    try:

        result = ask_gemini(prompt)

        critical = int(re.search(r"Critical:\s*(\d+)", result).group(1))
        medium = int(re.search(r"Medium:\s*(\d+)", result).group(1))
        minor = int(re.search(r"Minor:\s*(\d+)", result).group(1))

        return {
            "critical": critical,
            "medium": medium,
            "minor": minor,
            "total": critical + medium + minor
        }

    except Exception as e:

        return {
            "error": str(e)
        }