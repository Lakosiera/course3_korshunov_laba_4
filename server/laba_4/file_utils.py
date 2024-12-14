from base64 import b64encode
import time

STOTRAGE_FOLDER = "/storage"

def handle_uploaded_file(file, title):
    # формат имения "время_создания-имя_файла"
    filename=f"{int(time.time())}-{title}"
    # сгенерируем новое имя файла на основе алгоритма base64 чтобы
    base64 = b64encode(filename.encode()).rstrip().decode().replace("/", "_")

    with open(f"{STOTRAGE_FOLDER}/{base64}.json", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
