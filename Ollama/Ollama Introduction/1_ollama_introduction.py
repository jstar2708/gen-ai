from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:8b",
    temperature=0
)

ai_message = llm.invoke("Hi")
print(ai_message.content)