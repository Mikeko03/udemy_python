import json

data = {}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)