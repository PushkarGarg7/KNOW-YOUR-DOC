from langchain_text_splitters import CharacterTextSplitter
from langchain.docstore.document import Document


class TextToChunks:
    def __init__(self, text):
        self.text = text

    def split_text(self):
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=2500,
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False,
        )
        chunks = text_splitter.split_text(self.text)
        documents = [Document(page_content=chunk) for chunk in chunks]
        return documents
        
