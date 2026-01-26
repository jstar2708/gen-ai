from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.tools import tool, InjectedToolArg
from langchain_core.messages import HumanMessage
import requests
from typing import Annotated
from dotenv import load_dotenv
import json

load_dotenv()


@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """This function fetches the currency conversion factor between a given base currency and target currency"""
    url = f'https://v6.exchangerate-api.com/v6/28bd4cf89ed47355821657fa/pair/{base_currency}/{target_currency}'

    response = requests.get(url)

    return response.json()

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """
    given a currency conversion rate, this function calculates the target currency value from a given base currency value
    """

    return base_currency_value * conversion_rate

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.2", task="text-generation")

model = ChatHuggingFace(llm=llm)

llm_with_tools = model.bind_tools([convert, get_conversion_factor])

messages = [HumanMessage("What is the conversion factor between USD and INR, and based on that can you convert 10 USD to INR?")]

ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)

for tool_call in ai_message.tool_calls:
    # Execute the first tool and get value of conversion rate
    # Execute 2nd tool using the conversion rate from 1.
    if tool_call["name"] == "get_conversion_factor":
        tool_message_1 = get_conversion_factor.invoke(tool_call)
        # Fetch this conversion rate
        conversion_rate = json.loads(tool_message_1.content)['conversion_rate']
        # Append this tool message to messages list
        messages.append(tool_message_1)
    # 
    if tool_call['name'] == "convert":
        # Fetch the current arg
        tool_call['args']['conversion_rate'] = conversion_rate
        tool_message_2 = convert.invoke(tool_call)
        messages.append(tool_message_2)

result = llm_with_tools.invoke(messages).content
print(result)