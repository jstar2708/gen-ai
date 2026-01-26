from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings, ChatCohere
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Step 1a: Indexing (Document Ingestion)

video_id = "Gfr50f6ZBvo"  # Only the ID, not full URL
try:
    # If you don't care which language, this returns the "best" one.
    transcript_list = YouTubeTranscriptApi().fetch(video_id=video_id, languages=["en"])

    # Flatten it into plain text
    transcript = " ".join(chunk.text for chunk in transcript_list)
    print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video")

# Step 1b: Indexing (Text Splitting)
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

print(len(chunks))

# Step 1c and d: Indexing (Embedding generation and storing in Vector store)
embeddings = CohereEmbeddings(model="embed-english-v3.0")
vector_store = FAISS.from_documents(chunks, embeddings)

print(vector_store.index_to_docstore_id)

# Step 2: Retrieval
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
result = retriever.invoke("What is Deep mind?")
print(result)

# Step 3: Augmentation

llm = ChatCohere(temperature=0.2)
prompt = PromptTemplate(
    template="""
        You are a helpful assitant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
        Question: {question}
    """,
    input_variables=["context", "question"],
)

question = (
    "Is the topic of aliens discussed in this video? If yes then what was discussed?"
)
retrieved_docs = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
final_prompt = prompt.invoke({"context": context_text, "question": question})

print(final_prompt)

# Step 4: Generation

answer = llm.invoke(final_prompt)
print(answer)
