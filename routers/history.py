from fastapi import APIRouter
from utils.history import load_history

router = APIRouter()


@router.get("/history")
def get_history():

    try:
        history = load_history()

        return {
            "history": history
        }

    except Exception as e:

        return {
            "error": str(e)
        }