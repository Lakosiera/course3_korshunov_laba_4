from base64 import b64encode, b64decode
import time
from os import listdir, path
from pathlib import Path

STOTRAGE_FOLDER = "/storage"


def handle_uploaded_file(file, title):
    # формат имения "время_создания-имя_файла"
    filename = f"{int(time.time())}-{title}"
    # сгенерируем новое имя файла на основе алгоритма base64 чтобы
    base64 = b64encode(filename.encode()).rstrip().decode().replace("/", "_")

    with open(f"{STOTRAGE_FOLDER}/{base64}.json", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def read_dir():
    dir_list = listdir(path.abspath(STOTRAGE_FOLDER))
    result = []
    for file_name in dir_list:
        base_name=Path(file_name).stem.replace("_", "/")
        name=b64decode(base_name).decode().split("-", 1)
        result.append(name[1])
    return result

