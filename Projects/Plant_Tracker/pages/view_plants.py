import streamlit as st
import tool as mytool
import pandas as pd

st.header("View & Search Plants")

#upload data
plant_data=mytool.load_data("plants.csv")
activity_data=mytool.load_data("activity.csv")

#radio to select
type = st.radio(
    "search all or by name or location?",
    ["all","name", "location"] )

if type == "name":
     name=st.selectbox("select the plant", plant_data['name'].unique(),index=None, placeholder="Choose")  #store chosen name
     merge_data= pd.merge(plant_data,activity_data,left_on='name', right_on='plant') #merged activity + plant
     this_filter = merge_data["plant"] == name #filter
     result=merge_data[this_filter][["name","date_y","activity","height","location","water_freq","sunlight","season"]] #apply filter + choose cols
     st.write(result)
elif type=="location":
#select
    location=st.selectbox("select the plant", plant_data['location'].unique(),index=None, placeholder="Choose") 
    selected_loc= plant_data[plant_data["location"]==location]
    all_data= selected_loc[["name","date","location","water_freq","sunlight","season"]]
    st.write(all_data)

else:
    st.write(plant_data[["name","date","location","water_freq","sunlight","season"]])
