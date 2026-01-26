from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a Linkedin post about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Write a tweet about {topic}", input_variables=["topic"]
)

model = ChatCohere()
parser = StrOutputParser()
chain = RunnableParallel({
    'post': RunnableSequence(prompt1, model, parser),
    "tweet": RunnableSequence(prompt2, model, parser)
})
result = chain.invoke({"topic": "AI"})
print(result['tweet'])
print(result['post'])
