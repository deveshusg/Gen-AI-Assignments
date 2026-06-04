from pathlib import Path

def load_prompt(file_name: str) -> str:

    prompt_path = Path("prompts") / file_name

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()