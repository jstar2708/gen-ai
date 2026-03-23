import streamlit as st

st.title("Hello LLM App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your favourite variety of chai")

chai = st.selectbox("Your favourite: ", ["Masala Chai", "Adrak Chai", "Chocolate Chai"])
st.write(f"You choose {chai}!")

st.success("Your chai has been brewed")
