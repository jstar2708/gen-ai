from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-v3.1:671b-cloud",
    temperature=0
)

ai_message = llm.invoke("Name 10 great cricketers")
print(ai_message.content)