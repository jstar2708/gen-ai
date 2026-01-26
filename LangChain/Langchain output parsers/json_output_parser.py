from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V3.2',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)

# 1st Prompt -> Detailed report

parser = JsonOutputParser()

template1 = PromptTemplate(
    template='Give me name, age and city of a fictional person.\n {format_instruction}',
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)
prompt = template1.format()
print(prompt)

chain = template1 | model | parser
result = chain.invoke({})
print(result)

# Or you can write
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)