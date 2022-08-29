from json import JSONDecodeError
import requests


# payload = {"name": "Mike"}
response = requests.get('http://playground.learnqa.ru/api/get_text')
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text["answer"])
except JSONDecodeError:
    print("Наш ответ получен не в JSON формате")
finally:
    pass

print(response.status_code)