import json


string_as_format = '{"answer": "Hello, User"}'
obj = json.loads(string_as_format)
print(obj["answer"])