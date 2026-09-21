import streamlit as st

st.title("Plant Care Tracker☘️")

view_plants=st.Page("pages/view_plants.py", title="🌵All Plants")
search= st.Page("pages/search.py" ,title="👯Matching Care")
add_activity = st.Page("pages/add_activity.py", title="➕Add Activity")
add_plant = st.Page("pages/add_plant.py", title="➕Add Plant")
growth = st.Page("pages/growth.py", title="📐See Plant Growth")
season = st.Page("pages/season.py", title="❄️Seasonal Recommendations")
due_care = st.Page("pages/due_care.py", title="💊Plant Due Care")
doctor = st.Page("pages/doctor.py", title="🥼Ask Dr.Planty")

pg = st.navigation([view_plants,search,add_activity,add_plant,growth,season,due_care,doctor])
pg.run()

