import streamlit as st
st.title("Plant Care Tracker")

#import csv
import pandas as pd
plant = pd.read_csv('plants.csv')
print(plant.head(1))
