from crewai import Agent
from src.config import llm
from src.tools import pdf_tool, web_search_tool
from crewai.memory.unified_memory import Memory

# 1. The Router/Researcher Agent
researcher_agent = Agent(
    role="Lead AI Research Specialist",
    goal="Answer complex questions about the '{user_query}' by combining paper data and web research.",
    backstory=(
        "You are an expert at analyzing deep learning papers. Your strength is knowing "
        "when to trust the local PDF and when to verify information with a web search. "
        "You always provide citations for your findings."
    ),
    tools=[pdf_tool, web_search_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# 2. The Technical Writer/Validator Agent
writer_agent = Agent(
    role="Senior Technical Writer",
    goal="Synthesize research into a clear, structured, and accurate technical explanation.",
    backstory=(
        "You take raw research notes and turn them into professional documentation. "
        "You double-check that the terminology used is accurate "
        "and that the response is contextually relevant."
    ),
    llm=llm,
    verbose=True,
)