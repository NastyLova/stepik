from zipfile import ZipFile

with ZipFile('workbook.zip') as zip:
    files = list(filter(lambda x: not x.is_dir(), zip.infolist()))
    print(min(files, key=lambda x: x.compress_size/x.file_size).filename.split('/')[-1])