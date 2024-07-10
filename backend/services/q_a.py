from backend.PreProcessors.pdf_to_text import PDFToText
from backend.PreProcessors.textToChunks import TextToChunks
from backend.database.chroma_setup import setup_chroma_vector_db
from backend.database.session_db import get_session_data, set_session_data
from backend.models.qa_RAG import create_rag_chain, invoke_rag_chain
from io import BytesIO
import logging


def q_a(file_content, question, session_id):
    logging.debug(f"Session ID: {session_id}")
    session_data = get_session_data(session_id)
    logging.debug(f"Session Data Before Processing: {session_data}")
    
    if not session_data or 'vectorstore' not in session_data:
        logging.debug(f"Processing new file for session: {session_id}")
        extractor = PDFToText(file_content)
        extracted_text = extractor.extract_text()

        chunker = TextToChunks(extracted_text)
        chunks = chunker.split_text()
        
        vectorstore = setup_chroma_vector_db(chunks, session_id)
        set_session_data(session_id, {'vectorstore': vectorstore})
        logging.debug(f"New vectorstore created for session: {session_id}")
    else:
        logging.debug(f"Using existing vectorstore for session: {session_id}")
        vectorstore = session_data['vectorstore']

    retriever = vectorstore.as_retriever()
    rag_chain = create_rag_chain(retriever)
    answer = invoke_rag_chain(rag_chain, question, session_id)

    logging.debug(f"Answer generated for session {session_id}: {answer}")
    logging.debug(f"Session Data After Processing: {get_session_data(session_id)}")
    
    return answer