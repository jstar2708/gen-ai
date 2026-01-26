from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = [
    "Delhi is the captial of India",
    "I love cricket",
    "Kolkata is the capital of West Bengal",
]

embedding = CohereEmbeddings(model="embed-english-v3.0")
result = embedding.embed_documents(texts=documents)
print(result)
