import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from crewai import LLM

# Load environment variables (API Keys)
load_dotenv()

# --- 1. SHARED EMBEDDING MODEL ---
# Initialized once, reused by ChromaDB and any retrieval tools.
EMBEDDINGS = OllamaEmbeddings(model="qllama/bge-small-en-v1.5", temperature=0)

# --- 2. SHARED LLM ---
llm = LLM(model="ollama/kimi-k2.5:cloud", temperature=0, base_url="https://ollama.com")

# --- 3. VECTOR STORE FACTORY ---
CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "research_data"


def get_vectorstore():
    """Returns the existing ChromaDB instance."""
    if os.path.exists(CHROMA_DIR):
        return Chroma(
            persist_directory=CHROMA_DIR,
            embedding_function=EMBEDDINGS,
            collection_name=COLLECTION_NAME,
        )
    return None


def create_vectorstore():
    return Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=EMBEDDINGS,
        collection_name=COLLECTION_NAME,
    )
