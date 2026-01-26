from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.2", task="text-generation")

model = ChatHuggingFace(llm=llm)

class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment of the review either negitive, positive, or neutral"]


structured_model = model.with_structured_output(Review)
result = structured_model.invoke("""
Technology has become an essential part of our daily life.
It helps us communicate, learn, and work more efficiently.
From smartphones to the internet, it saves time and effort.
When used wisely, technology makes life easier and smarter.
""")

print("Summary: ", result['summary'])
print("Key Themes: ", result['key_themes'])
print("Sentiment: ", result['sentiment'])