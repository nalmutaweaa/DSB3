import streamlit as st
import tool as mytools
import pandas as pd

st.header("Seasonal Advice for your plants")
#container1 
with st.container(height=500):
    today=pd.to_datetime("today").month #get month
    this_season= mytools.get_season(today)
    st.header(f'Now is {this_season} Season!!')
    if this_season == "Winter":
        st.snow()
        st.write("Rely on hardy greens like kale, or structured evergreens like boxwood and holly for steady color.")
    elif this_season == "Spring":
        st.write("🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷")
        st.write(" Grow colorful blooms like tulips, daffodils, and hyacinths, or warm-weather annuals like marigolds and zinnias")
    elif this_season == "Summer":
        st.write("🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞")
        st.write("Grow heat-loving vegetables like tomatoes, peppers, and zucchini, alongside petunias and geraniums.")
    else:
        st.write("🍂🍂🍂🍂🍂🍂🍂🍂🍂🍂🍂🍂🍂🍂")
        st.write("Plant cool-weather crops like broccoli, cauliflower, and garlic. Add autumn flowers like mums, pansies, and asters.")
    st.header("Focus on these plants!")
    st.write(mytools.recommend_plant(this_season))

#container2: climate choose and recommend plants
with st.container(height=500):
    st.header("Choose your climate and get plant recommendations")
    import requests
    url = "https://house-plants2.p.rapidapi.com/all-lite"

    headers = {
        "x-rapidapi-key": "d0b1d3a15cmsh292562406931275p1eedf4jsn1a25becb2197",
        "x-rapidapi-host": "house-plants2.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    plants_api= response.json()
    plants_df= pd.DataFrame(plants_api)

    #choose your cilmate
    climate=st.selectbox("Select your climate",plants_df['Climat'].unique())
    matching_climate=plants_df[plants_df["Climat"]==climate]
    st.write(matching_climate[["Common name","Climat","Origin"]]) #display only these

#container 3: for adjusting water 
with st.container(height=500):
    #get plant name,season,freq
    st.header("Adjust your watering frequency based on the season")
    plant_data = mytools.load_data("plants.csv")
    name= st.selectbox("select the plant",plant_data['name'].unique()) #display exisiting plants
    plant_season= plant_data.loc[plant_data["name"] == name, "season"].iloc[0] #take season
    plant_water= plant_data.loc[plant_data["name"]==name, "water_freq"].iloc[0] #take water

    #display results
    st.write(f'Plant: {name}')
    st.write(f'Perfered Season: {plant_season}')
    st.write(f'Normal Watering Frequency: {plant_water}')

    new_req=mytools.adjuest_watering(name, this_season,plant_season,plant_water)
    st.write(new_req)
