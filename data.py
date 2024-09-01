# part three   How to display data on streamlit
import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1,2,3,4,5,6,7,8]
n = np.array(a);
nd = n.reshape((2,4))
dic = {
    "NAME" : ["KHYAL","DEWARE"],
    "AGE" : [21,32],
    "CITY" : ["JABALPUR","BANGLORE"]
}
data = pd.read_csv(r"C:\Users\khyal\Desktop\streamlit\Salary_Data.csv")
print(data)

st.dataframe(n)
st.dataframe(nd)
st.dataframe(dic)
st.dataframe(data)
st.dataframe(data, width=2000, height=500) #these are height and width of the displayed table
st.table(dic)
st.json(dic)
# write(var) can identify the data type of var, and will print output accordingly  
st.write(data)  # write() will automatically identify data and print it in dataframe format
st.write(a)     # write() will automatically identify a and print it in array format
st.write(dic)   # write() will automatically identify dic and print it in json format

# cacheing mechanism use krne se poora ka poora script ko execute krna pdta, basically time saving krta hai
@st.cache_data # this is called cache decorator
def ret_time(a):
    time.sleep(5)
    return time.time() 

if st.checkbox("1"):  # this will create a checkbox 1
    st.write(ret_time(1))

if st.checkbox("2"):    # this will create a checkbox 2
    st.write(ret_time(2))




