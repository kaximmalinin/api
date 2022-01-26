import requests
URL = "http://127.0.0.1:5000/predict"
requests.get("http://127.0.0.1:5000/")
response = requests.post(URL, json='{"text":"Понравилось обслуживание банка, вежливые сотрудники и все доступно объяснили."}')
print ("Понравилось обслуживание банка, вежливые сотрудники и все доступно объяснили.")
print(response.json()["answer"][1:-1])
response = requests.post(URL, json='{"text":"Мошенники! Все было ужасно. Мне нахамили и не дали кредит"}')
print ("Мошенники! Все было ужасно. Мне нахамили и не дали кредит.")
print(response.json()["answer"][1:-1])
