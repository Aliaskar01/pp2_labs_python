import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, 'data.json')

with open(file_path, 'r') as file:
    data = json.load(file)

array = []

for item in data['imdata']:
    if "l1PhysIf" in item:
        array.append(item["l1PhysIf"])

for i in range(3):
    print(
        array[i]["attributes"]["dn"], 
        array[i]["attributes"]["speed"], 
        array[i]["attributes"]["mtu"]
)