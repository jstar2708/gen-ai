from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the following joke.\n{joke}", input_variables=["joke"]
)

model = ChatCohere()
parser = StrOutputParser()
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)
result = chain.invoke({"topic": "AI"})
print(result)
