from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader(file_path='LangChain\Langchain Document Loaders\dl-curriculum.pdf')
docs = loader.load()
print(len(docs))
print(docs[0].metadata)

