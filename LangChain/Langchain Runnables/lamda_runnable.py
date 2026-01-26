from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_classic.schema.runnable import (
    RunnableSequence,
    RunnablePassthrough,
    RunnableParallel,
    RunnableLambda,
)

load_dotenv()


def word_count(text):
    return len(text.split())


prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

model = ChatCohere()
parser = StrOutputParser()
joke_gen_chain = RunnableSequence(prompt1, model, parser)
parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableLambda(word_count),
    }
)
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
result = final_chain.invoke({"topic": "AI"})
print(result)
