from backend.PreProcessors.pdf_to_text import PDFToText
from backend.PreProcessors.textToChunks import TextToChunks
from backend.database.chroma_setup import setup_chroma_vector_db
from backend.database.session_db import get_session_data, set_session_data
from backend.models.qa_RAG import create_rag_chain, invoke_rag_chain

def q_a(file_path, question, session_id):
    session_data = get_session_data(session_id)
    
    if session_data:
        # Retrieve stored data
        vectorstore = session_data['vectorstore']
    else:
        # Process the PDF
        extractor = PDFToText(file_path)
        extracted_text = extractor.extract_text()

        # Create chunks
        chunker = TextToChunks(extracted_text)
        chunks = chunker.split_text()
        
        # Setup vector database
        vectorstore = setup_chroma_vector_db(chunks)

        # Store the vectorstore in session data
        set_session_data(session_id, {'vectorstore': vectorstore})

    # Create the retriever from vectorstore
    retriever = vectorstore.as_retriever()

    # Create the RAG chain
    rag_chain = create_rag_chain(retriever)

    # Answer the question using the RAG chain
    answer = invoke_rag_chain(rag_chain, question, session_id)

    return answer
