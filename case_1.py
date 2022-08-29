import requests


response = requests.get('http://playground.learnqa.ru/api/check_type')

print(response.text)