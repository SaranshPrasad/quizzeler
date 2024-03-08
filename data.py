import requests

API_URL = "https://opentdb.com/api.php"
PARAMS = {
    "amount": 1000,
    "type": "boolean"
}

response = requests.get(url=API_URL, params=PARAMS)
data = response.json()
question_data = data["results"]