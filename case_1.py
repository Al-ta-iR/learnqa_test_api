import requests


payload = {"name": "Mike"}
response = requests.get('http://playground.learnqa.ru/api/check_type', params=payload)

print(response.text)