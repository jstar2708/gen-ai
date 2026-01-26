from langchain_community.document_loaders import TextLoader
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatCohere()

prompt = PromptTemplate(
    template="Write a summary for the following poem.\n{poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader(file_path='LangChain\Langchain Document Loaders\cricket.txt',encoding='utf-8')
docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({"poem": docs[0].page_content})
print(result)


