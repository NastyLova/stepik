from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip', 'r') as zip:
    files = sorted(list(filter(lambda x: not x.is_dir(), zip.infolist())), key=lambda x: x.filename.split('/')[-1])
    for file in files:
        print(f'''{file.filename.split('/')[-1]}
  Дата модификации файла: {datetime(*file.date_time)}
  Объем исходного файла: {file.file_size} байт(а)
  Объем сжатого файла: {file.compress_size} байт(а)
''')