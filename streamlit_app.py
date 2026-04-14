import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng


st.title('Dashboard')
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("These headers have rotating dividers", divider=True)

with st.sidebar:
    st.header("SideBar")
    st.write("This is the sidebar!")


col1, col2 = st.columns(2)

with col1:

    x = st.slider("Choose x value", 1, 10)

st.write("The value of x is", x)

with col2:

    st.write("The value of x is", x)

df = pd.DataFrame(
    {
        "col1": list(range(20)),
        "col2": rng(0).standard_normal(20),
        "col3": rng(1).standard_normal(20),
    }
)

st.area_chart(
    df,
    x="col1",
    y=["col2", "col3"],
    color=["#FF000080", "#0000FF80"],
)
