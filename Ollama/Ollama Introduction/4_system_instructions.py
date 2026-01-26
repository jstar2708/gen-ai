from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model='deepseek-r1:8b'
)

messages = [
    SystemMessage(
        content="You are a Financial Advisor. Do not answer any other questions which are not related to finance."
    ),
    HumanMessage(
        content="What is financial analysis?"
    )
]

stream = llm.stream(messages)

for chunk in stream:
    print(chunk.text, end='')