from langchain_classic.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = """

Forwarded this email? Subscribe here for more
How to Become Data Engineer in 2026 (Zero To Senior)
Built from 17 years of real data engineering experience
Data with Baraa
Jan 20

 




READ IN APP
 
Hey friends - Happy Tuesday!

Last year, I shared a roadmap on how to become a data engineer. I honestly did not expect the impact it would have. Many of you followed it step by step, and some of you even told me you landed your first job.

So I went back and reviewed the entire roadmap. I updated it based on today’s market and extended it.

This time, it does not stop at getting hired. It shows what to learn after you join a company, from Junior to Senior, and eventually to Data Architect.
"""

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 10,
    separator=''
)

result = splitter.split_text(text)
print(result)

loader = PyPDFLoader(
    file_path='Langchain Document Loaders\dl-curriculum.pdf'
)
docs = loader.load()

result = splitter.split_documents(docs)
print(result[0])