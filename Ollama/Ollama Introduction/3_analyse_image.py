from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
import base64

image_path = 'Ollama\\media\\133888652902752941.jpg'

with open(image_path, "rb") as f:
    image_bytes = f.read()
image_64 = base64.b64encode(image_bytes).decode("utf-8")

image_input = HumanMessage(
    content=[
        {"type": "text", "text": "Describe this Image"},
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{image_64}"},
        },
    ]
)

llm = ChatOllama(model="gemma3:4b")

response = llm.invoke([image_input])
print(response.content)