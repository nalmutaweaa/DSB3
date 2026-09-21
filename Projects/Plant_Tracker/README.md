# Plant Care Tracke
_Topic: Plant Tracker_
# Project Description 

Plant Care Tracker is a simple application that helps users manage and monitor their plants and their care activities.
The app allows users to add plants, record care activities, monitor plant growth, check watering reminders, search and compare plants, get seasonal recommendations, and ask an AI assistant for plant-care advice.
Plant information and activity records are stored in CSV files.

## Main Features

### 🌵 All Plants

View all plants stored in the application.

Users can also search and filter plants by name or location and view their saved details and activity history.

### 🧑‍🤝‍🧑 Matching Care

Select a plant and find other plants with similar care requirements.

The matching is based on:
- Watering frequency
- Sunlight needs
- Preferred season

### ➕ Add Activity

Record a new care activity for an existing plant.

Activities include:
- Watering
- Fertilizing
- Repotting
- Pruning

Users can also enter the date, plant height, and a progress picture.

### ➕ Add Plant

Add a new plant to the collection by entering:
- Plant name or species
- Location
- Date
- Watering frequency
- Sunlight requirement
- Preferred season

The plant is then added to `plants.csv`.

### 📐 See Plant Growth

Track the growth of a selected plant using its recorded height over time.

The page displays the plant's dates and heights in a line chart so the user can see whether the plant is growing, staying stable, or decreasing.

Progress pictures can also be displayed.

### ❄️ Seasonal Recommendations

Provides care suggestions based on the current season.

The page:
- Detects the current season
- Gives general seasonal advice
- Shows plants from the user's collection that match the current season
- Uses an external plant API to recommend plants based on climate
- Adjusts watering frequency depending on seasonal changes

### 🩹 Plant Due Care

Shows plants that are currently due for watering.

The application checks the latest watering date for each plant and compares it with its watering frequency.

If the number of days since the last watering is greater than or equal to the watering frequency, the app displays a reminder.

### 🧚 Ask Dr. Planty

An AI plant-care assistant.

The user selects a plant and enters a question or symptom. The selected plant's information and activity history are passed to the LLM to provide possible causes, care advice, and a suggested recovery plan.

## Data

The application stores plant information in:

- `plants.csv`

Plant activity records are also stored in CSV format.

## Technologies Used

- Python
- Streamlit
- Pandas
- RapidAPI
- OpenRouter