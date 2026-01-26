from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


model = ChatCohere()

class Review(BaseModel):
    key_themes: list[str] = Field(
        description="Write down all the key themes discussed in the review"
    )
    summary: str = Field(description="A brief summary of the review")
    sentiment: str = Field(
        description="Return sentiment of the review either negitive, positive, or neutral"
    )


structured_model = model.with_structured_output(Review)
result = structured_model.invoke(
    """
Technology has become an essential part of our daily life.
It helps us communicate, learn, and work more efficiently.
From smartphones to the internet, it saves time and effort.
When used wisely, technology makes life easier and smarter.
"""
)

print("Summary: ", result.summary)
print("Key Themes: ", result.key_themes)
print("Sentiment: ", result.sentiment)
