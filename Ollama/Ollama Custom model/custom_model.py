# 
# Run the following command to create the custom model.
# ollama create sentiment:latest -f Ollama/Ollama\ Custom\ model/Modelfile

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "sentiment:latest"
)

result = llm.invoke("This course is really bad")
print(result.content)