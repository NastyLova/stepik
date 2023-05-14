from zipfile import ZipFile

def get_size(size):
    '''
    По размеру файла определяем максимальную единицу измерения и возвращаем строку с размером в этой единице + сама единица измерения
    :param size: размер файла в байтах
    :return: размер файла в самых крупных единицах измерения с округлением до целых
    '''
    sizes = str(size)
    if size == 0:
        return None

    if size < dict_dimension['KB']:
        sizes += ' B'
    elif dict_dimension['KB'] <= size < dict_dimension['MB']:
        sizes = str(round(size / dict_dimension['KB'])) + ' KB'
    elif dict_dimension['MB'] <= size < dict_dimension['GB']:
        sizes = str(round(size / dict_dimension['MB'])) + ' MB'
    elif dict_dimension['GB'] <= size:
        sizes = str(round(size / dict_dimension['GB'])) + ' GB'

    return sizes

dict_dimension = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
with ZipFile('desktop.zip', 'r') as zip:
    # Структура уже такая как нужно, отбираю только наименования и размеры файлов
    files = list(map(lambda x: [x.filename.strip('/').split('/'), x.file_size], zip.infolist()))

    for file in files:
        size = get_size(file[1])
        # Если это не файл, а папка, то размер будет 0, функция вернет None
        print('  ' * (len(file[0]) - 1) + file[0][-1], size if size else '')