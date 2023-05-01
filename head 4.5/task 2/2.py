from zipfile import ZipFile

with ZipFile('workbook.zip') as zip:
    files = list(filter(lambda x: not x.is_dir(), zip.infolist()))
    files_size = sum([file.file_size for file in files])
    sizes_compress = sum([file.compress_size for file in files])
    print(f'''Объем исходных файлов: {files_size} байт(а)
Объем сжатых файлов: {sizes_compress} байт(а)''')