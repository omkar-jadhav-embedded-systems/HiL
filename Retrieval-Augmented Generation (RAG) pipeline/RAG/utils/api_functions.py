import requests
import json
from dotenv import load_dotenv
import os
from utils.prompts import PROMPT_TEMPLATE
from pathlib import Path

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST")
MODEL = os.getenv("MODEL")

OUTPUT_DIR = Path(os.getcwd())/"generated_tests"
OUTPUT_DIR.mkdir(exist_ok=True)

def generate_test_rag(query, context):
    """
    Generates test code using retrieved RAG context.
    """
    prompt = PROMPT_TEMPLATE.format(context=context).strip()

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": True
    }

    print(f"\n🚀 Generating test for: {query}")
    print("------------------------------------------------")

    full_output = ""

    with requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json=payload,
        stream=True
    ) as response:

        response.raise_for_status()

        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                text = chunk.get("response", "")
                print(text, end="", flush=True)
                full_output += text
                if chunk.get("done"):
                    break

    test_file = OUTPUT_DIR / f"test_{query}.py"
    test_file.write_text(full_output.strip())

    print(f"\n\n✅ Generated: {test_file}")
