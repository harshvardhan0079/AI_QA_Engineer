from pathlib import Path
from utils.gemini import ask_gemini

class CodeAnalyzer:

    def analyze_file(self, file_path):

        code = Path(file_path).read_text(encoding="utf-8")

        prompt = f"""
You are a Senior Python QA Engineer.

Analyze this code and return:

1. Bugs
2. Security Issues
3. Code Smells
4. Best Practices
5. Quality Score (/10)

Code:

{code}
"""

        return ask_gemini(prompt)