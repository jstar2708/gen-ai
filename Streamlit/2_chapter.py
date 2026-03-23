import streamlit as st

st.title("Chai maker app")

if st.button("Make chai"):
    st.success("Your chai is brewed")

add_masala = st.checkbox("Add masala")

if add_masala:
    st.write("Masala added to your chai")

tea_type = st.radio("Pick your chai base : ", ['Milk', 'Water', 'Honey'])
st.write(f"You selected {tea_type}")

flavour = st.selectbox("Choose flavour: 0", ['adrak', 'kesar', 'Tulsi'])
st.write(f"Selected flavour {flavour}")

sugar = st.slider("Sugar level", 0, 5, 1)
st.write(f"Sugar level {sugar}")

cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"Total cups: {cups}")

name = st.text_input("Enter you name")
if name:
    st.write(f"Welcome, {name}!, your chai is on way")

dob = st.date_input("Select your DOB")
st.write(f"Your DOB is: {dob}")