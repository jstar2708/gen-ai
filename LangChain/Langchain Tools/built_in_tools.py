from langchain_community.tools import DuckDuckGoSearchRun

# DuckDuckGo Search
search_tool = DuckDuckGoSearchRun()
results = search_tool.invoke("Top news in India Today")
print(results)

# Shell Tool
from langchain_community.tools import ShellTool
shell_tool = ShellTool()
result = shell_tool.invoke("whoami")
print(result)

