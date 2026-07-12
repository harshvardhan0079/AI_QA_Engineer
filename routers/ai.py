from fastapi import APIRouter

from utils.gemini import ask_gemini
from models.schemas import Prompt

router = APIRouter()

@router.post("/ask")
def ask(prompt: Prompt):
    answer = ask_gemini(prompt.prompt)
    return {
        "response": answer
    }

@router.get("/ai")
def ai():
    answer = ask_gemini("Explain Python in simple Hindi.")
    return {
        "response": answer
    }