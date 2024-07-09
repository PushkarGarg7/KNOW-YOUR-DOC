# Ensure this file contains something like this:


# from backend.models.gemini import google_llm  # Correct import path

from langchain_core.prompts import PromptTemplate  # Corrected import as per warning
from langchain.schema import StrOutputParser


from langchain_google_genai import ChatGoogleGenerativeAI
import os
import getpass

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("api_key")

google_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
def get_summarization_chain():
    llm = google_llm
    prompt_template = """Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:"""
    prompt = PromptTemplate.from_template(prompt_template)

    return (
        prompt       # Prompt for Gemini
        | llm        # Gemini function
        | StrOutputParser()  # Output parser
    )
