import requests


# payload = {"name": "Mike"}
response = requests.get('http://playground.learnqa.ru/api/hello', params={"name": "Mike"})
parsed_response_text = response.json()

print(parsed_response_text["answer"])