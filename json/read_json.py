import json


with open("data.json") as j:
    data = json.load(j)
ma = "email"
print(data["facebook"][ma])