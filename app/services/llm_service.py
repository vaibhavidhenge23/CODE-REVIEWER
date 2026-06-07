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
    template="""
You are an expert code reviewer. Review the following {language} code.

Provide feedback in this exact JSON format:
{{
  "summary": "brief overall assessment",
  "issues": [
    {{
      "severity": "critical/warning/suggestion",
      "line": "line number or general",
      "issue": "what is wrong",
      "fix": "how to fix it"
    }}
  ],
  "refactored_code": "improved version of the code",
  "score": "score out of 10"
}}

Code to review:
{code}

Return ONLY the JSON, no extra text.
"""
)

def review_code(code: str, language: str) -> dict:
    chain = prompt | llm
    response = chain.invoke({"code": code, "language": language})
    return response.content