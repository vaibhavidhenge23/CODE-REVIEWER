from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt = PromptTemplate(
    input_variables=["code", "language"],
    template="""Review this {language} code. Return ONLY valid JSON, no markdown.

{{
  "summary": "one line assessment",
  "score": "X/10",
  "issues": [
    {{
      "severity": "critical|warning|suggestion",
      "line": "line number or general",
      "issue": "what is wrong",
      "why": "root cause simple words",
      "quick_fix": "fastest fix",
      "best_fix": "production level fix"
    }}
  ],
  "refactored_code": "improved code"
}}

Code:
{code}"""
)

def review_code(code: str, language: str) -> dict:
    chain = prompt | llm
    response = chain.invoke({"code": code, "language": language})
    return response.content