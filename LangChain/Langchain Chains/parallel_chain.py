from langchain_cohere import ChatCohere
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.schema.runnable import RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following topic.\n{topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a short quiz on the following topic.\n{topic}",
    input_variables=['topic']
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document.\nNotes -> {notes}\nQuiz ->\n{quiz}",
    input_variables=['notes', 'quiz']
)

model1 = ChatCohere()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.2", task="text-generation")
model2 = ChatHuggingFace(llm=llm)


parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({"topic": "Linear regression"})
chain.get_graph().print_ascii()
print(result)