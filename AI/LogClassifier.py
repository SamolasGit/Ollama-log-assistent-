import ollama
import json

MODEL = "qwen2.5:3b"

def analyze_log(log_text: str) -> dict:
    prompt = f"""
You are a senior software engineer.

Return ONLY valid JSON with this exact schema:
{{
  "root_cause": "...",
  "error_type": "...",
  "fix_suggestion": "..."
}}

LOG:
{log_text}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        format="json"
    )

    return json.loads(response["message"]["content"])


log = """
ERROR 2025-12-13 21:32:01 DatabaseError: connection refused
at db.connect (db.js:42)
"""

result = analyze_log(log)
print(result)
