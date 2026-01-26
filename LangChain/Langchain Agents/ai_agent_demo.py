from langchain_cohere import ChatCohere
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv

load_dotenv()

search_tool = DuckDuckGoSearchRun()
results = search_tool.invoke("Top news in India today")

llm = ChatCohere()

from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic import hub

# Pull the ReAct prompt from LangChain Hub
prompt = hub.pull("hwchase17/react")    # Pulls the standard ReAct agent prompt

# Create the react agent
agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

# Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

# Invoke
response = agent_executor.invoke({"input": "3 ways to reach goa to Delhi"})
print(response)