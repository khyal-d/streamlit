# part one
import streamlit as st

st.title("Hello Streamlit")

# part two
st.header("Header")
st.subheader("Sub header")
st.text("Like this video and subscribe to the channel")
st.markdown(""" # h1 tag
## h2 tag
### h3 tag
:moon: \n
:sunglasses: \n
Syntax for emphasise are **asterisks** and _underscores_ and ~~Scratch this.~~.
""",True)

st.latex(r''' a + ar + ar^2 + ar^3 + \cdots + ar^{n-1} =
          \sum_{k=0}^{n-1} ar^k =
          a \left(\frac{1-r^{n}}{1-r}\right) ''') # r means the string written is raw

st.write("khyal","deware","python")
st.write("# khyal","deware","python")
st.write(st, width=500, height=500)
st.write(sum)

d = {
    "NAME" : "KHYAL",
    "LANGUAGE" : "PYTHON",
    "TOPIC" : "STREAMLIT"
}
st.write(d)





