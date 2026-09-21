import streamlit as st
import tool as mytool
st.header("record your plant activities🪴💦🌱")
#read csv 
activity_data = mytool.load_data("activity.csv")
plants_data=mytool.load_data("plants.csv")

#f1: adding activity
#name,activity, date,img,height
with st.form("new_activity_form"):
	name = st.selectbox("select the plant", plants_data['name'].unique()) #display exisiting plants
	activity = st.selectbox("Enter Activity", ["Watering", "Fertilizing", "Repotting", "Pruning"])
	date = st.date_input("Enter Date")
	picture = st.camera_input("Take a picture")
	height = st.number_input("Enter Plant Height in cm", value=1.0)

	submitted = st.form_submit_button(label="Add Activity")
if submitted:
	if picture is not None:
		img_path="images/" + picture.name
		with open(img_path,"wb") as file:
			file.write(picture.getbuffer())
	else:
		img_path=""
	mytool.add_activity(name, activity, date, picture, height)
	st.success("Added")
