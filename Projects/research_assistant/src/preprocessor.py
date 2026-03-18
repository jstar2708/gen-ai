from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.pdf import PyPDFLoader
from src.config import get_vectorstore, create_vectorstore

headers_to_split_on = [
    ("#", "Title"),
    ("##", "Section"),
    ("###", "Subsection"),
]


class Preprocessor:
    def __init__(
        self,
        filepath,
    ):
        self.document_loader = PyPDFLoader(filepath)
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=700,
            chunk_overlap=70,
            length_function=len,
            is_separator_regex=False,
            separators=[
                "\n\n",
                "\n",
                " ",
                "",
            ],  # Priority: Paragraphs -> Lines -> Words
        )
        self.output_path = filepath
        print(self.output_path)

    def create_chunks_and_save_to_db(self):
        # Load PDF as documents
        docs = self.document_loader.load()

        # Split documents
        splitted_docs = self.splitter.split_documents(docs)

        # Create vector store and save documents
        vector_store = get_vectorstore()
        if not vector_store:
            vector_store = create_vectorstore()
        vector_store.add_documents(splitted_docs)
