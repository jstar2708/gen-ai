from langchain_cohere import ChatCohere
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv

load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""
    return a * b

# Tool binding
llm = ChatCohere()
llm_with_tools = llm.bind_tools([multiply])
result = llm_with_tools.invoke("Hi how are you?")

# Tool calling
query = HumanMessage("Can you multiply 3 with 1000")
messages = [query]
result = llm_with_tools.invoke(messages)
messages.append(result)

# Tool execution
result = multiply.invoke(result.tool_calls[0])
messages.append(result)

final_result = llm_with_tools.invoke(messages)
print(final_result)
