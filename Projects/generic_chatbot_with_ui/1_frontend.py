import streamlit as st
from langchain_core.messages import HumanMessage
from backend_1 import chatbot

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type here...")
if user_input:
    with st.chat_message("user"):
        st.session_state["message_history"].append(
            {"role": "user", "content": user_input}
        )
        st.text(user_input)

    config = {"configurable": {"thread_id": 1}}
    ai_message = chatbot.invoke(
        {"messages": [HumanMessage(content=user_input)]}, config=config
    )
    ai_message = ai_message["messages"][-1].content
    with st.chat_message("ai"):
        st.session_state["message_history"].append(
            {"role": "ai", "content": ai_message}
        )
        st.text(ai_message)
