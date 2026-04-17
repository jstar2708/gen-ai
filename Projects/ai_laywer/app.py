from data_loader import (
    load_knowledge_base,
    get_const_collection,
    get_property_collection,
)
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

load_knowledge_base()


def get_system_prompt():
    with open(
        "C:\\Projects\\Gen AI\\Projects\\ai_laywer\\prompt\\system_prompt.txt", "r"
    ) as f:
        return SystemMessage(content=f.read())


prop_col = get_property_collection()
const_col = get_const_collection()

messages = [get_system_prompt()]

user_query = input("Enter your query?\n")

prop_result = prop_col.query(query_texts=[user_query], n_results=5)
const_result = const_col.query(query_texts=[user_query], n_results=3)

context = f"USER QUERY: - {user_query}\n\n"

context += "RELEVANT PROPERTY RECORD:- \n"
for doc in prop_result.get("documents"):
    context += doc[0] + "\n"

context += "RELEVANT CONSTITUTIONAL LAW:- \n"
for doc in const_result.get("documents"):
    context += doc[0] + "\n"

messages.append(HumanMessage(content=context))

llm = ChatOllama(model="deepseek-v3.1:671b-cloud", temperature=0)

result = llm.invoke(messages)
import io
import sys
# Forces the terminal output to use UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print(result.content)
