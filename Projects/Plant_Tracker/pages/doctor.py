import streamlit as st
import tool as mytools


st.title("🧑‍⚕️🌿Dr: Planty")
st.header("Ask your AI doctor about your plants")
#form take user input text
with st.form("llm_form"):
    activity_data= mytools.load_data("activity.csv")
    plant_name = st.selectbox("Select your plant", activity_data['plant'].unique())
    #get information about the plant
    get_info = mytools.get_info(plant_name)
    
    txt = st.text_area(
    "Type your question here")
    prompt = f'plant is {plant_name} care activity about the plant are {get_info}user concern is {txt}'

    submitted= st.form_submit_button(label="Submit")
if submitted:
    result = mytools.get_llm_response(prompt)
    st.write(result)