# from backend.PreProcessors.pdf_to_text import PDFToText
# from backend.models.summarization_chain import get_summarization_chain

# def summarize_pdf(file_path):
#     # Load PDF and extract text
#     extractor = PDFToText(file_path)
#     extracted_text = extractor.extract_text()

#     # Get the summarization chain and invoke it
#     summarization_chain = get_summarization_chain()
#     return summarization_chain.invoke(extracted_text)




from backend.PreProcessors.pdf_to_text import PDFToText
from backend.models.summarization_chain import get_summarization_chain
from io import BytesIO

def summarize_pdf(file_content):
    # Load PDF and extract text
    extractor = PDFToText(file_content)
    extracted_text = extractor.extract_text()

    # Get the summarization chain and invoke it
    summarization_chain = get_summarization_chain()
    return summarization_chain.invoke(extracted_text)

