from langchain_community.vectorstores import Chroma
from langchain_cohere import CohereEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()
# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(
        page_content="Chroma is a vector database optimized for LLM-based search."
    ),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# Step 2: Initialize embedding model
embedding_model = CohereEmbeddings(model="embed-english-v3.0")

# Step 3: Create Chroma vector store
vector_store = Chroma.from_documents(
    documents=documents, embedding=embedding_model, collection_name="my_collection"
)

# Step 4: Convert vector store into a retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

query = "What is Chroma used for?"
results = retriever.invoke(query)
for i, doc in enumerate(results):
    print(f"\n------Result {i + 1}-----")
    print(doc.page_content)
