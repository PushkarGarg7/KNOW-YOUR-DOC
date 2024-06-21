from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("AIzaSyAQS7AkkwmTYJ8GXjbqM0PgfZ_iZS-BDG0")

# Directly use the API key
# GEMINI_API_KEY = 
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def setup_chroma_vector_db(chunks):
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
    return vectorstore
