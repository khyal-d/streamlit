# part four Displaying Plots and Media
import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt 
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)


st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)


plt.scatter(data['a'], data['b'])
# plt.title("scatter")
st.pyplot() #st.pyplot for streamlit, plt.show for regular python script


chart = alt.Chart(data).mark_circle().encode( 
    x = 'a', y = 'b', tooltip = ['a', 'b']
    )
st.altair_chart(chart, use_container_width=True)


st.graphviz_chart("""
digraph{
    watch -> like
    like -> share
    share -> subscribe 
    share -> watch
}
""")


city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})
st.map(city)
st.map()



st.image(r"C:\Users\khyal\Pictures\Screenshots\Screenshot (124).png")
st.audio(r"C:\Users\khyal\Music\Shri Hanuman Chalisa.mp3")
st.video(r"https://www.youtube.com/watch?v=YyAuFiIv-V4")


