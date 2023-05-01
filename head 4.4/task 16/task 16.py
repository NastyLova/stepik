import json

with open('food_services.json', 'r', encoding='utf-8') as f:
    js = json.load(f)
    types = {}

    for obj in js:
        if obj['TypeObject'] not in types:
            types[obj['TypeObject']] = max(list(filter(lambda x: x['TypeObject'] == obj['TypeObject'], js)), key=lambda x: int(x['SeatsCount']))

    for key, value in sorted(types.items()):
        print(f'{key}: {value["Name"]}, {value["SeatsCount"]}')