from langchain_cohere import ChatCohere
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatCohere()


st.header("Research Tool")
user_input = st.text_input("Enter you prompt")
if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
