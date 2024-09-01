# Adding layout to your streamlit app
import streamlit as st

st.title("Registration Form")

first, last = st.columns(2) # this creates two text input boxes of equal size/area in the same row
first.text_input("Fisrt Name")
last.text_input("Last Name")

email, mob = st.columns([3,1]) # this creates two text input boxes having ratio of size/area as 3:1 in the same row
email.text_input("Email ID")
mob.text_input("Mob number")

user, pw, pw2 = st.columns(3)
user.text_input("Username")
pw.text_input("Password", type = "password") # type = password makes the password invisible
pw2.text_input("Retype Your Password", type = "password")

# here we kept bl1, bl2, bl3 as intentionally blank, so that cb and submit can be at left and right corners
cb, bl1, bl2, bl3, submit = st.columns(5)
cb.checkbox("I Agree")
submit.button("Submit")