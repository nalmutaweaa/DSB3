import streamlit as st
import pandas as pd
import tool as mytools

st.header("Plants Growth Tracker📐")
#load data
activity_data = mytools.load_data("activity.csv")
#ask user plant name
name = st.selectbox("select the plant", activity_data['plant'].unique()) #display exisiting plants
#filter
this_filter = activity_data[activity_data["plant"] == name]
growth_data = this_filter[["date", "height"]] #take only date _height
growth_data['date'] = pd.to_datetime(growth_data['date'], format="mixed") #convert
if growth_data.empty:
    st.write("No growth data available for this plant...")
else:
    st.write(growth_data)

#growth chart
st.line_chart(
    growth_data,
    x="date",
    y="height"
)



