from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.reddit.com/r/Medium/comments/1bu58pc/ai_flooding_medium/'
loader = WebBaseLoader(url)
docs = loader.load()
print(len(docs))
print(docs[0].page_content)