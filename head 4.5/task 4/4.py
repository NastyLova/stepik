from zipfile import ZipFile
from datetime import datetime

date_filter = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
with ZipFile('workbook.zip') as zip:
    # фильтруем данные. Отбираем только те, что не являются директориями и подходят по дате
    files = list(filter(lambda x: not x.is_dir() and datetime(*x.date_time) > date_filter, zip.infolist()))
    # Достаем только названия файлов и фильтруем их
    files = sorted(list(map(lambda x: x.filename.split('/')[-1], files)))
    # Принтуем названия файлов
    print(*files, sep='\n')