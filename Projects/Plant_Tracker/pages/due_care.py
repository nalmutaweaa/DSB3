import streamlit as st
import pandas as pd
import tool as mytools

st.header("Plants need attention🍂")

#upload data
plant_activity= mytools.load_data("activity.csv")
plants=mytools.load_data("plants.csv")
#call due care function
care= mytools.due_care()
for plant in care:
    st.write(plant)