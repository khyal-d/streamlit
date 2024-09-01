#Adding dynamic widgets
import streamlit as st

st.title("WIDGETS")
st.button("Non functional button")
if st.button("A Functional Button"):
    st.write("You just clicked the button")

name = st.text_input("NAME")
st.write(name)

address = st.text_area("Enter your address")
st.write(address)

st.date_input("Enter a date")
st.time_input("Enter a time")

st.checkbox("i agree to t&c", value = False) # checkbox is empty bcz value = False
st.checkbox("i agree to t&c", value = True) # checkbox will already be ticked bcz, value is set to be true
if(st.checkbox("do you agree to t&c")):
    st.write("you agreed!!")

v1 = st.radio("Colours", ['r', 'g', 'b'], index=0) # checkbox of 'r' will already be ticked bcz, index is set to be 0, 0 is key to 'r'
v2 = st.selectbox("Colours", ['r', 'g', 'b'], index=1) # 'g' will already be selected bcz, index is set to be 1, 1 is key to 'g'
st.write(v1, v2)

#now selecting multiple options
v3 = st.multiselect("Colours", ['r', 'g', 'b'])
st.write(v3)

#adding a slider
st.slider("AGE", min_value=18, max_value=60, value=30, step=10) # step=10 means, 18 se 28, 28 se 38, 38 se 48, ....
st.number_input("NUMBERS", min_value=18.00, max_value=60.00, value=30.00, step=5.00) # make sure to pass float values over here

im = st.file_uploader("Upload a file here!")
st.image(im)