from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-pro-preview",
)
response = llm.invoke("What is the captial of India?")
print(response.content)
