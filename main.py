### Ensure the environment variable is set in the same terminal session where the Python script runs.
### when the terminal is closed the environment variable will be vanished as it is temporary.

import requests
import datetime as dt
import os
Application_ID = os.environ.get('application_id')
Application_Keys = os.environ.get('application_keys')
nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

Sheety_username = os.environ.get('sheety_username')
Sheety_password = os.environ.get('sheety_password')
Sheety_url = os.environ.get('sheety_url')

headers = {
    "x-app-id": Application_ID,
    "x-app-key": Application_Keys,
    "Content-Type": "application/json"
}

data = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": 55,
    "height_cm": 172,
    "age": 23
}

response = requests.post(nutritionix_url, json=data, headers=headers)
response.raise_for_status()
# resp = []
is_ok = False

if response.status_code == 200:
    datas = response.json().get("exercises", [])
    if data:
        for data in datas:
            exercise = data["name"].title()
            duration = data["duration_min"]
            calories = data["nf_calories"]
            today = dt.datetime.today().strftime("%d-%m-%Y")
            time = dt.datetime.today().strftime("%I:%M:%S %p")
            sheet_data = {
                "sheet1": {
                    "date": today,
                    "time": time,
                    "exercise": exercise,
                    "duration": duration,
                    "calories": calories
                }
            }
            response = requests.post(Sheety_url, json=sheet_data, auth=(Sheety_username, Sheety_password))
            if response.status_code == 200:
                is_ok = True
                # resp += requests.get(Sheety_url, auth=(Sheety_username, Sheety_password)).text
            else:
                print("Error:", response.status_code, response.text)
    else:
        print("No exercises found in the response.")
else:
    print("Error:", response.status_code, response.text)

# print(resp)
if is_ok:
    print("Data added to Google Sheet successfully!")