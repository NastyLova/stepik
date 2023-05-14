from zipfile import ZipFile
import json

with ZipFile('data.zip', 'r') as zip:
    result = []
    files = list(map(lambda x: x.filename, list(filter(lambda x: x.filename.split('.')[-1].lower() == 'json', zip.infolist()))))
    for file in files:
        with zip.open(file) as f:
            try:
                js = json.loads(f.read().decode('utf-8'))
                if js['team'] == 'Arsenal':
                    result.append(f'''{js['first_name']} {js['last_name']}''')
            except:
                pass
    print(*sorted(result), sep='\n')
