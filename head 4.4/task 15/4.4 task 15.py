import json

with open('food_services.json', 'r', encoding='utf-8') as r:
    js = list(json.load(r))
    districts = {}
    nets = {}

    for obj in js:
        districts[obj['District']] = districts.get(obj['District'], 0) + 1
        if obj['IsNetObject'] != 'нет':
            nets[obj['OperatingCompany']] = nets.get(obj['OperatingCompany'], 0) + 1
    max_district = max(districts.items(), key=lambda x: x[1])
    max_net = max(nets.items(), key=lambda x: x[1])

    print(f'''{max_district[0]}: {max_district[1]}
{max_net[0]}: {max_net[1]}''')
