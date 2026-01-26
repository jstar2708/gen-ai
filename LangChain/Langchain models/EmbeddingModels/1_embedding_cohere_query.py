from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = CohereEmbeddings(model="embed-english-v3.0")
result = embedding.embed_query("Delhi is the capital of India.")
print(result)
