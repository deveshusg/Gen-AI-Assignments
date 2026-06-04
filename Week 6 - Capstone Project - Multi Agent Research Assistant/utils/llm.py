from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm():
    """
    Returns configured OpenAI LLM instance.
    """

    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )