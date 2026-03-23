import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    vote1 = st.button("Vote Masala Chai")


with col2:
    st.header("Adrak Chai")
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting Masala Chai")
if vote2:
    st.success("Thanks for voting Adrak Chai")

st.image("https://images.pexels.com/photos/20214512/pexels-photo-20214512/free-photo-of-hand-holding-bundle-of-item-over-pot-on-burning-bonfire.jpeg?auto=compress&cs=tinysrgb&h=400&fit=crop&crop=focalpoint&dpr=2", width=200)

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala","Kesar", "Adrak"])
st.sidebar.write(f"Welcome {name} your {tea} chai is getting ready!")

with st.expander("Show chai making instructions"):
    st.write("""
1. Boil water
2. Add milk
3. Done!
""")
    

st.markdown("### Welcome to Chai app")
st.markdown('> Block quote')