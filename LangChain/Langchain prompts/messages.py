from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_cohere.chat_models import ChatCohere
from dotenv import load_dotenv

load_dotenv()

model = ChatCohere()
messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about LangChain")
]
result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)