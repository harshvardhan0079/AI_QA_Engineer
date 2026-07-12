from fastapi import APIRouter
import json

from models.schemas import ScoreRequest
from utils.gemini import ask_gemini
from utils.history import save_history
from utils.pdf_generator import generate_pdf_report

router = APIRouter()


@router.post("/quality-score")
def quality_score(request: ScoreRequest):

    prompt = f"""
You are a Senior Python QA Engineer.

Analyze the following Python code.

Return ONLY valid JSON.

Format:
{{
    "quality_score": 0,
    "security": 0,
    "performance": 0,
    "readability": 0,
    "maintainability": 0,
    "summary": ""
}}

Python Code:
{request.code}
"""

    try:

        result = ask_gemini(prompt)

        result = (
            result.replace("```json", "")
                  .replace("```", "")
                  .strip()
        )

        analysis = json.loads(result)

    except json.JSONDecodeError:

        return {
            "error": "Gemini returned invalid JSON.",
            "raw_response": result
        }

    except Exception as e:

        return {
            "error": str(e)
        }

    pdf_path = generate_pdf_report(
        filename="User_Code",
        analysis=analysis
    )

    save_history(analysis)

    return {
        "analysis": analysis,
        "pdf_report": pdf_path
    }