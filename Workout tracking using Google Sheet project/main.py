import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 175.26
AGE = 25

APP_ID = "9ccdc1e3"
API_KEY = "781dd577adc6259147c3b5125c3b6871"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
add_row = "https://api.sheety.co/"
projectName = "MyWorkout"
sheetName = "workouts"
username= "1buKRaAhe-6U_tBOpOZmGFrnBP44KkD4JI2IFINB1-Qk"
exercise_text = input("Tell me which exercises you did: ")
sheet_endpoint = "https://api.sheety.co/be780702df84abff4b48a0d2d69ef82e/myWorkout/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()['exercises']

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for loops in result:
    exercise = loops['name'].title()
    duration = loops['duration_min']
    calories = loops['nf_calories']

# ran 3 miles and walked 3 km
    sheet_input = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    header = {
        "Authorization": "Basic cHl0aG9uLnRlc3Q6YEV4dik2aH5zPkVHNXJqYg==",
    }
    response = requests.post(sheet_endpoint, json=sheet_input, headers=header)
    text = response.text
    sheet_rep = response.json()
    print(sheet_rep)
