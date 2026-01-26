from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
text = "Delhi is the capital of India"
vector = embedding.embed_query(text)
print(str(vector))
