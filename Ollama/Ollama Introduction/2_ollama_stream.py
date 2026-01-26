from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:8b"
)

stream = llm.stream("Who are you?")
for chunk in stream:
    print(chunk.text, end='')
