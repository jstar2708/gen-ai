from crewai.tools import BaseTool
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings
from typing import Type
from pydantic import BaseModel, Field
from src.config import EMBEDDINGS, llm, get_vectorstore
from crewai_tools import TavilySearchTool


# 3. Create the Custom Tool Class for CrewAI
class PDFSearchSchema(BaseModel):
    """Input for PDFSearchTool."""

    query: str = Field(
        ..., description="The technical question to search for in the research paper."
    )


class PDFResearchTool(BaseTool):
    name: str = "Search a PDF's content"
    description: str = (
        "A tool that can be used to semantic search a query from a PDF's content."
    )
    args_schema: Type[BaseModel] = PDFSearchSchema

    def _run(self, query: str) -> str:
        # Search the vector store for the top 3 most relevant chunks
        docs = get_vectorstore().similarity_search(query, k=3)

        # Combine the content into a single string for the Agent to read
        result = "\n\n".join(
            [f"Source (Page {d.metadata['page']}): {d.page_content}" for d in docs]
        )
        return result

# 4. Instantiate the tool
pdf_tool = PDFResearchTool()

# 5. Web search Tool
web_search_tool = TavilySearchTool(max_results=3)