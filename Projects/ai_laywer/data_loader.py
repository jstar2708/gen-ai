from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_community.document_loaders.json_loader import JSONLoader
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
import chromadb
import dotenv
import uuid

from chromadb.utils import embedding_functions


# 1. Define what to extract from each JSON object
def extract_metadata(record: dict, metadata: dict) -> dict:
    metadata["article"] = record.get("article")
    metadata["title"] = record.get("title")
    return metadata


def load_knowledge_base():
    # Setting up Ollama Embedding model and Chroma DB
    # Initialize the Chroma-native Ollama EF
    # This object correctly implements the .name() and __call__ protocols
    ollama_ef = embedding_functions.OllamaEmbeddingFunction(
        model_name="bge-m3",
    )

    client = chromadb.PersistentClient(path="./property_vault")

    # Creating two collections to keep data clean
    prop_col = client.get_or_create_collection(
        name="property_data", embedding_function=ollama_ef
    )
    const_col = client.get_or_create_collection(
        name="indian_constitution", embedding_function=ollama_ef
    )

    if prop_col.count() == 0:
        # Load and Index your 14 Property MD files (Hindi)
        prop_loader = DirectoryLoader(
            path="C:\Projects\Gen AI\Projects\\ai_laywer\data\property",
            glob="./*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
        )
        prop_docs = prop_loader.load()

        for doc in prop_docs:
            id = str(uuid.uuid4())
            prop_col.add(
                documents=[doc.page_content],
                ids=[id],
                metadatas=[{"source": doc.metadata["source"], "lang": "hi"}],
            )
            print(f"Added property document with ID: {id}")
    if const_col.count() == 0:
        # Load and Index Constitution of India (JSON)
        const_loader = JSONLoader(
            file_path="C:\Projects\Gen AI\Projects\\ai_laywer\data\constitution\constitution_of_india.json",
            jq_schema=".[]",
            content_key="description",
            metadata_func=extract_metadata,
        )
        const_docs = const_loader.load()

        for doc in const_docs:
            id = f"article_{doc.metadata['article']}"
            const_col.add(
                ids=[id],
                documents=[doc.page_content],
                metadatas=[doc.metadata],
            )
            print(f"Added constitution article with ID: {id}")

        print("Knowledge base loaded successfully!..")


def get_property_collection():
    return chromadb.PersistentClient(path="./property_vault").get_or_create_collection(
        name="property_data"
    )


def get_const_collection():
    return chromadb.PersistentClient(path="./property_vault").get_or_create_collection(
        name="indian_constitution"
    )
