from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import getpass
import os
import logging

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("api_key")

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
chroma_client = Chroma()


def setup_chroma_vector_db(chunks, session_id):
    collection_name = f"langchain_{session_id}"  # Unique collection name based on session ID
    logging.debug(f"Setting up Chroma vector store with chunks for session: {session_id}")
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, collection_name=collection_name)
    logging.debug("Chroma vector store setup complete")
    # chroma_client.delete_collection(collection_name)
    # print(chroma_client._collection.get())

    # logging.debug(f"Chroma collections: {collections['data']}")
    return vectorstore