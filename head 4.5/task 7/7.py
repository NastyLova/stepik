from zipfile import ZipFile
import os.path as p

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('files.zip', 'w') as zip:
    for file in file_names:
        size = p.getsize(file)
        if size <= 100:
            zip.write(file)