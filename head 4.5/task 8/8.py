from zipfile import ZipFile

def extract_this(zip_file, *agrs):
    with ZipFile(zip_file, 'r') as zip:
        if len(agrs) == 0:
            zip.extractall()

        files = list(filter(lambda x: x.filename.split('/')[-1] in agrs, zip.infolist()))
        for file in files:
            zip.extract(file)
