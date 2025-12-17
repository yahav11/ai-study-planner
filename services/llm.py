import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI


ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(f"OPENAI_API_KEY is missing. Expected it in: {ENV_PATH}")

client = OpenAI(api_key=api_key)


def generate_study_plan(prompt: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return resp.choices[0].message.content


