from langchain_huggingface.embeddings.huggingface_endpoint import (
    HuggingFaceEndpointEmbeddings,
)
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
)

query_result = embeddings.embed_query("My name is Jaideep")
print(query_result)
