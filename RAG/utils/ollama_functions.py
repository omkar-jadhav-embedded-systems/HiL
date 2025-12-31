import subprocess
import requests
from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST")
MODEL = os.getenv("MODEL")
OLLAMA_EXE = os.getenv("OLLAMA_EXE")

def check_ollama_running():
    try:
        r = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=5)
        r.raise_for_status()
        print("✅ Ollama server is running")
        return True
    except Exception as e:
        print(f"❌ Ollama not reachable: {e}")
        return False


def pull_model(model):
    print(f"📥 Ensuring model '{model}' is available...")
    subprocess.run([OLLAMA_EXE, "pull", model], check=True)