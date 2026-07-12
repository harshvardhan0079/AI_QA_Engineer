import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in .env")

client = Groq(api_key=API_KEY)

print("✅ Groq API Loaded")


class GeminiError(Exception):
    pass


def ask_gemini(prompt: str) -> str:
    """
    Keeping the same function name so the rest of the project
    doesn't need any changes.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        raise GeminiError(str(e))