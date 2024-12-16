import time
from datetime import datetime
from os import listdir, path, remove
from .models import ExportFile

# директория для хранения медиафайлов
STOTRAGE_FOLDER = "/storage"


# метод для записи файла
def write_file(file, title):
    # формат имения "время_создания-имя_файла"
    filename = f"{int(time.time())}-{title}"

    # открыть файл для "w" - записи, "b" - как бинарный файл
    with open(f"{STOTRAGE_FOLDER}/{filename}", "wb+") as destination:
        # для каждого "кусочка" (chunk) данных
        for chunk in file.chunks():
            # записываем в 
            destination.write(chunk)


# метод для чтения файла
def read_file(filename):
    # открыть файл для "r" - чтения, "b" - как бинарный файл
    return open(f"{STOTRAGE_FOLDER}/{filename}", 'rb')


# метод для удаления файла
def delete_file(filename):
    file = f"{STOTRAGE_FOLDER}/{filename}"
    # если файл существует
    if path.exists(file):
        # удаляем
        remove(file)


# метод для чтения директории
def read_dir():
    # читаем содержимое директории
    dir_list = listdir(path.abspath(STOTRAGE_FOLDER))
    # подгатавливаем пустой список результата
    result = []
    # перебираем все имена файлов из директории
    for filename in dir_list:
        # разделяем име по первому встречному символу "-"
        # чтобы получить время создания и оригинальное имя файла
        name = filename.split("-", 1)
        # добавляем в результат обьект с данными файла
        result.append(
            # создаем экземпляр можели для экспорта файла
            ExportFile.create(
                title=name[1], # имя для отображения
                filename=filename, # полное имя файла
                created_at=to_date(name[0]) # дата создания
            )
        )
    # возврвщвем результат
    return result


# метод для преобразования timestamp (1734359992) в привычный формат дата-время
def to_date(text):
    try:
        # преабразуем строку с timestamp в целое число
        timestamp=int(text)
        # получаем дату из timestamp
        return datetime.fromtimestamp(timestamp)
    except ValueError:
        # если что то пошло не так возвращаем текущую дату
        return time.time()
    