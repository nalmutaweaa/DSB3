import streamlit as st
import pandas as pd
import tool as mytool

st.header("add your new plant to the collection!🌿")
#read csv
data=mytool.load_data("plants.csv")

#form taking user input
with st.form("new_plant_form"):
	name= st.text_input("Enter Plant Name / Species ")
	location= st.text_input("Enter location")
	date= st.datetime_input("Enter Date")
	water_freq= st.number_input("Enter Watering frequency in days", value=1)
	sunlight= st.selectbox("Sunlight needed", ["Low", "Medium", "High"])
	season= st.selectbox("Plant season", ["Summer", "Winter", "Fall","Spring"])
	
	submitted= st.form_submit_button(label="Add Plant")
if submitted:
#call function from tools
     mytool.add_plants(name,location,date,water_freq,sunlight, season)
     st.success("Added")
