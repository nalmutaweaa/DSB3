import pandas as pd
import streamlit as st


#load data
def load_data(path):
    "this function loads csv data"
    df= pd.read_csv(path)
    return df

#f1: add function
def add_plants(name,location,date,water_freq,sunlight,season):
    "thic function adds and stores new planys to csv"
    plant=pd.read_csv('plants.csv')
    new_plant = pd.DataFrame([{
    "name":name,
    "location":location,
    "date":date,
    "water_freq": water_freq,
    "sunlight":sunlight,
    "season": season
}])
    plant= pd.concat([plant,new_plant],ignore_index=True)
    plant.to_csv('plants.csv') #store

#f2 : add activity 
def add_activity(name,activity,date,img,height):
    "this function adds new activity in activity csv"
    activity_data=pd.read_csv('activity.csv')
    new_activity = pd.DataFrame([{
    "plant":name,
    "activity":activity,
    "date":date,
    "img": img,
    "height":height
}])
    activity_data= pd.concat([activity_data,new_activity],ignore_index=True)
    activity_data.to_csv('activity.csv',index=False) #store

# f3: needs care
def due_care():
    "this function displays plants due care"
    due_care=[] 
    today= pd.to_datetime("today") #get today date
    activity_data=pd.read_csv("activity.csv")
    activity_data["date"] = pd.to_datetime(activity_data["date"],format="mixed")
    plant_data=pd.read_csv('plants.csv')
    for plant, water_freq in zip(plant_data["name"], plant_data["water_freq"]):
        watering= activity_data[(activity_data["plant"] == plant) & (activity_data["activity"] == "Watering")] 
        if watering.empty:
            continue
        last_watered = (today - watering["date"].max()).days   # 21/9- 10/9 =9days ago watered
        if last_watered >= water_freq: # 9>3 => mint every 3 days but 9 last = late 
            due_care.append(f'{plant} needs watering! It has been {last_watered} days since the last watering.')
    return due_care
#f4: doctor
from openai import OpenAI
#from dotenv import load_dotenv
#import os
#load_dotenv('.env')
openai_api_key = st.secrets['api_key']
if not openai_api_key:
    raise RuntimeError("API KEY is not configured")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= openai_api_key
)
#get plant info
def get_info(plant_name):
    "this functions gets selected plant activities to be passed as prompt"
    activity_data=pd.read_csv('activity.csv')
    info=activity_data[activity_data['plant']== plant_name]
    return info


def get_llm_response(prompt):
    "this functions passes user prompt and returns llm response"
    completion = client.chat.completions.create(
        model="cohere/north-mini-code:free",
        
        messages=[
            {
                "role": "system",
                "content": "You are a plant expert, provide one time advice and to generate adiagnostic report and step-by-step recovery plan.information about plant care dont ask follow up questions.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response

#f5: get the season 
def get_season(today):
    "this function returns which season we are at based on today's date"
    if today in [12,1,2]:
        season="Winter"
        st.snow()
    elif today in[3,4,5]:
        season="Spring"
    elif today in [6,7,8]:
        season="Summer"
    else:
        season="Fall"
    return season

def recommend_plant(season):
    "get the plant recommended for this season from my csv"
    plant_data=pd.read_csv('plants.csv')
    recommended_plants= plant_data[plant_data['season']== season]
    return recommended_plants['name'].unique()


def adjuest_watering (name, this_season,plant_season,plant_water):
    "this function adjuse watering frequency based on season"
    new_freq=0
    #sunlight
    if plant_season == this_season:
        return f'Keep the same watering frequency: every{plant_water}  day'
    elif this_season =="Summer":
        new_freq = plant_water - 2 #more water
        return f'Since its {this_season}, increase watering freq to" every {new_freq} days'
    elif this_season == "Winter":
        new_freq= plant_water + 2 #less water
        return f'Since its {this_season}, adjust watering frequency to: every {new_freq} days'
    elif this_season == "Fall":
        new_freq= plant_water -1 #more water
        return f'Since its {this_season}, adjust watering frequency to: every {new_freq} days'
    else:
        new_freq= plant_water + 1 #less water
        return f'Since its {this_season}, adjust watering frequency to:every {new_freq} days'


def matching(name,water_freq,sunglight,season):
    "this function returns matching plants based on ater_freq,sunglight,season"
    plant_data=pd.read_csv("plants.csv")
    matching = plant_data[
        (plant_data["water_freq"] == water_freq)
        & (plant_data["sunlight"] == sunglight)
        & (plant_data["season"] == season)
        &(plant_data["name"]!=name)
    ]
    return matching['name'] 