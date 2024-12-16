import time
from datetime import datetime
from os import listdir, path
from .models import ExportFile

STOTRAGE_FOLDER = "storage"


def handle_uploaded_file(file, title):
    # формат имения "время_создания-имя_файла"
    filename = f"{int(time.time())}-{title}"

    with open(f"{STOTRAGE_FOLDER}/{filename}", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def read_file(filename):
    return open(f"{STOTRAGE_FOLDER}/{filename}", 'rb')


def read_dir():
    dir_list = listdir(path.abspath(STOTRAGE_FOLDER))
    result = []
    for filename in dir_list:
        name = filename.split("-", 1)
        result.append(
            ExportFile.create(
                title=name[1],
                filename=filename,
                created_at=to_date(name[0])
            )
        )
    return result


def to_date(text):
    timestamp=0
    try:
        timestamp=int(text)
        pass
    except ValueError:
        pass
    date = datetime.fromtimestamp(timestamp)
    return date