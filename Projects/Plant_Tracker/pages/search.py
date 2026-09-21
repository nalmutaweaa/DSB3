import streamlit as st
import tool as mytool
#read csv 
activity_data = mytool.load_data("activity.csv")
plants_data=mytool.load_data("plants.csv")
#search by name
st.header("Search matching plants!")
name=st.selectbox("select the plant", plants_data['name'].unique(),index=None, placeholder="Choose") 
selected_name= plants_data[plants_data["name"]==name]

if selected_name.empty:
    st.write("you have to selece")
else:
    water_freq=selected_name["water_freq"].iloc[0]
    sunlight= selected_name ["sunlight"].iloc[0]
    season= selected_name["season"].iloc[0]
    result=mytool.matching(name,water_freq,sunlight,season)

    st.write(f'Matching plants with {name}')
    st.write(result)
    st.write(f'these plants need:')
    st.write(f'Watering every {water_freq} days')
    st.write(f'{sunlight} Sunlight')
    st.write(f'Prefered season is {season}')


