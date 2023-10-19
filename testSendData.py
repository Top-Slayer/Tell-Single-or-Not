import json

value = True
# a Python object (dict):
data = {
    "turning": bool(f'{value}'),
    }

with open(r'Control_sensor\data.json', 'w') as json_file:
    json.dump(data, json_file)

print(data)
