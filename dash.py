import streamlit as st
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt 
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

data = pd.read_csv(r"C:\Users\khyal\Desktop\streamlit\Salary_Data.csv")

# ML Model training
x = np.array(data["YearsExperience"]).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data["Salary"]))

st.title("Eperience vs Salary")

nav = st.sidebar.radio("Navigation", ["Home", "Prediction", "Contribution"])

if(nav == "Home"):

    st.image(r"C:\Users\khyal\Desktop\streamlit\sal.jpg", width=800)

    if(st.checkbox("show data")):
        st.table(data)

    graph = st.selectbox("What kind of GRAPH you want?", ["Non Interactive", "Interactive"], index=0)

    val = st.slider("Filter data using years", 0, 20)
    data = data[data["YearsExperience"]>=val] # filtering of data

    if(graph == "Non Interactive"):
        plt.figure(figsize=(10,5))
        plt.scatter(data["YearsExperience"], data["Salary"])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
#The plt.tight_layout() function in Matplotlib is used to automatically adjust the spacing between subplots to prevent overlapping of plot elements (like labels, titles, and ticks). When using Matplotlib within a Streamlit app, plt.tight_layout() can help ensure that your plots are neatly presented.
        plt.tight_layout() 
        st.pyplot()

    if(graph == "Interactive"):
        # Define the layout
        layout = go.Layout(
            xaxis = dict(range=[0,16], title="Years of Experience"),
            yaxis = dict(range=[0,210000], title="Salary"),
            title = "Salary vs. Years of Experience"
        )
        # Create the figure
        fig = go.Figure(
            data = go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode="markers"),
            layout = layout
        )
        st.plotly_chart(fig)



if(nav == "Prediction"):
    st.header("Know your Salary")
    val = st.number_input("Enter your Experience", 0.00, 20.00, step = 0.25)
    val = np.array(val).reshape(1,-1) # reshaped to 1 row and as may columns (-1) as needed
    pred = lr.predict(val)[0]
    if(st.button("PREDICT")):
        st.success(f"Your predicted salary is {round(pred)}")

if(nav == "Contribution"):
    st.header("Contribute to our dataset")
    st.subheader("Please fill in the form below")
    exp = st.number_input("Enter your experience", 0.00, 20.00)
    sal = st.number_input("Enter your salary", 0.00, 100000.00, step = 1000.00)
    if(st.button("SUBMIT")):
        to_add = {"YearsExperience" : [exp], "Salary" : [sal]}
        to_add = pd.DataFrame(to_add)
        # Append DataFrame to CSV file
        to_add.to_csv(r"C:\Users\khyal\Desktop\streamlit\Salary_Data.csv", mode='a', header=False, index=False)
        # Display a success message in Streamlit
        st.success("Data successfully submitted!")