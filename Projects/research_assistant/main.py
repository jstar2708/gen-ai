from crewai import Crew, Task, Process
from src.config import llm
from src.agents import researcher_agent, writer_agent
from src.preprocessor import Preprocessor
from dotenv import load_dotenv
from crewai.memory.unified_memory import Memory

load_dotenv()

# 1. Define the Research Task
# This fulfills "Intelligently route" and "Retrieve relevant information"
research_task = Task(
    description=(
        "Research the following topic: {user_query}. "
        "First, check the PDF paper for details. "
        "If the information is not there or if the user is asking for broader context,"
        " use the web search tool to supplement your findings. "
        "Provide a detailed set of research notes."
    ),
    expected_output="A structured list of facts and citations.",
    agent=researcher_agent,
)

# 2. Define the Synthesis & Validation Task
# This fulfills "Generate accurate responses" and "Validate quality"
synthesis_task = Task(
    description=(
        "Using the research notes provided, create a final answer for the user. "
        "Ensure that technical terms are used correctly. "
        "The response should be structured, professional, and directly address the user's query. "
        "If the researcher found conflicting info, prioritize the PDF for architectural facts."
    ),
    expected_output="A 3-4 paragraph technical explanation with a 'Sources' section at the end.",
    agent=writer_agent,
    context=[research_task],  # This ensures the writer sees the researcher's work
)

# 3. Assemble the Crew
research_crew = Crew(
    agents=[researcher_agent, writer_agent],
    tasks=[research_task, synthesis_task],
    process=Process.sequential,  # Researcher finishes -> Writer starts
    verbose=True,
    memory=Memory(
        llm="ollama/kimi-k2.5:cloud",
        embedder={"provider": "ollama", "config": {"model_name": "qllama/bge-small-en-v1.5:latest"}},
    ),
)

# 4. Run the Assistant
if __name__ == "__main__":
    print("--- Intelligent Agentic Research Assistant is Online ---")

    filepath = input("Please provide the PDF path (without quotes): ")
    preprocessor = Preprocessor(filepath)
    preprocessor.create_chunks_and_save_to_db()

    while True:
        # Example input as per your "Attention is all you need" use case
        user_input = input("Enter your query (\\bye for EXIT): ")
        if user_input == "\\bye":
            print("Exiting....")
            break

        result = research_crew.kickoff(inputs={"user_query": user_input})

        print("\n\n########################")
        print("## RESPONSE ##")
        print("########################\n")
        print(result)
