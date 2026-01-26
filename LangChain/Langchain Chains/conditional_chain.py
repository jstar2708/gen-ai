from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_classic.schema.runnable import RunnableBranch, RunnableLambda

load_dotenv()


class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(
        description="Give the sentiment of the feedback"
    )


model = ChatCohere()

parser = StrOutputParser()

pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following text.\n {text}\n{format_instruction}",
    input_variables=["text"],
    partial_variables={"format_instruction": pydantic_parser.get_format_instructions()},
)

classifer_chain = prompt1 | model | pydantic_parser

prompt2 = PromptTemplate(
    template="Write and appropriate response to the positive feedback.\n{feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Write and appropriate response to the negitive feedback.\n{feedback}",
    input_variables=["feedback"],
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "Negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment"),
)

chain = classifer_chain | branch_chain
result = chain.invoke({"text": "This is a terrible phone"})
print(result)