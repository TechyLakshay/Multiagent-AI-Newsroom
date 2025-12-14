# agents/reporter.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
#load .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# 🔑 Use your Gemini API key directly (not safe for prod, but fine for college demo)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key,
)

# Prompt to make summary short + factual
prompt = PromptTemplate.from_template(
    "Summarize this news headline in 4-5 factual lines:\n\n{headline}"
)

def generate_summary(headline: str) -> str:
    """
    Reporter Agent:
    Takes a news headline and generates a summary using Gemini.
    """
    _input = prompt.format(headline=headline)
    resp = llm.invoke(_input)
    return resp.content.strip()

# Quick test
if __name__ == "__main__":
    test = "Heavy rains cause flash floods in Delhi; several bridges closed"
    print("SUMMARY:", generate_summary(test))
