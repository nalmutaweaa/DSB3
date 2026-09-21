import streamlit as st
st.title("Plant Care Tracker")

#import csv
import pandas as pd
plant = pd.read_csv('plants.csv')
st.write(plant)


with st.form("new_plant_form"):
	
	name= st.text_input("Enter Planzt /species ")
	location= st.text_input("Enter location")
	date= st.datetime_input("Enter Date")
	water_freq= st.number_input("Enter Watering frequency in days")
	sunlight= st.selectbox("Sunlight needs", ["Low", "Medium", "High"])
		
	submitted= st.form_submit_button(label="Submit")
if submitted:
	new_plant = pd.DataFrame([{
		"name":name,
		"location":location,
		"date":date,
		"water_freq": water_freq,
		"sunlight":sunlight
}])

#add new_plant data to plant
	
	plant= pd.concat([plant,new_plant],ignore_index=True,inplace=True)
	st.write(plant)


def addPlant(name,location,date,water,sunlight):
	name = st.text_input("Enter Plant name/species ")
	location = st.text_input("Enter location")
	date = st.text_input("Enter Date")
	water = st.text_input("Enter Watering frequency in days")
	sunlight = st.text_input("Sunlight needs (Low, Medium, High)")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")