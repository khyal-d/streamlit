#adding widget to sidebar
import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt 

plt.style.use("ggplot") #

data = {
    "num" : [x for x in range(1,11)],
    "square" : [x**2 for x in range(1,11)],
    "twice" : [x*2 for x in range(1,11)],
    "thrice" : [x*3 for x in range(1,11)]
}

rad = st.sidebar.radio("Navigation", ["Home", "About us"])


if(rad == "Home"):
    df = pd.DataFrame(data = data)

    st.sidebar.selectbox("Select a number ", [1,2,3,4,5])

    col = st.sidebar.selectbox("Select a Column ", df.columns)
    plt.plot(df['num'], df[col])
    st.pyplot()

    multicol = st.sidebar.multiselect("Select a Column ", df.columns)
    plt.plot(df['num'], df[multicol])
    st.pyplot()


if(rad == "About us"):
    st.write("You are in about us page")
# now using some animations like, progress bars, status messages, and also baloon animation given by streamlit
   
    #showing progress bar. import time for this
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)

    #as soos as about us is selected, and progress bar is finished, we show a baloon animation
    st.balloons()

    #these are five status messages
    st.error("Error")
    st.success("Show Success")
    st.info("Information")
    st.exception(RuntimeError("This is an error"))
    st.warning("This is a warning")
    
    
    



