from langchain_cohere import ChatCohere
from dotenv import load_dotenv

load_dotenv()

llm = ChatCohere(temperature=0)
response = llm.invoke("What is the capital of India?")
print(response.content)
