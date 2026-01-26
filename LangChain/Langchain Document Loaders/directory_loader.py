from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='Langchain Document Loaders',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()
print(len(docs))

# docs = loader.lazy_load()
# for doc in docs:
#     print(doc.metadata)