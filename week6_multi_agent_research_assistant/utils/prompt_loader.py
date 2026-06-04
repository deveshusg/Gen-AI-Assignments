from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def load_prompt(file_name):

    prompt_path = (
        BASE_DIR
        / "prompts"
        / file_name
    )

    with open(
        prompt_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()