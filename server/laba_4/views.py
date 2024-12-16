from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.contrib import messages
from .forms import ImportFileForm
from .file_utils import write_file, read_file, read_dir, delete_file


# имя куки для хранения номера вкладки
COOKIE_ACTIVE_TAB="active_tab"


# пример простейшей вьющки
def hello_world(request):
    # простейший вывод html страницы
    return HttpResponse("Hello, world!")


# вьбшка главной страници
def index(request):
    # читаем список всех файло бля отображения во вкладке экспорт
    files = read_dir()
    # получаем из куки на какой вкладке мы были
    tab_index = request.COOKIES.get(COOKIE_ACTIVE_TAB, "0")
    # передаем данные контекста
    context = {
        # параметр заголовока
        "name": "Laba 4 - Музыкальные альбомы",
        # список файлов
        "files": files,
        # интекс вкладки
        "tab_index": tab_index,
    }
    # ренедр вьюшки в html страницу
    return render(request, "index.html", context)


# вьюшка для создания альбома
# она не отображает свою страницу а перенаправляет на главную
def create(request):
  # создаем ответ с редиректом на главную страницу
    response = HttpResponseRedirect(  # создаем редирект
        reverse(
            # имя редиреакта из "urls.py"
            "index"
        )
    )
    # устанавливаем в куки что это первая вкладка
    response.set_cookie(COOKIE_ACTIVE_TAB, 0)
    return response


# вьюшка для импорта файла
# она не отображает свою страницу а перенаправляет на главную
def upload_file(request):
    # проверяем что медод запроса "POST"
    if request.method == "POST":
        # получаем данные фолрмы из запроса
        form = ImportFileForm(request.POST, request.FILES)
        
        # проверяем что форма верна
        if form.is_valid():
            # вытаскиваем данные файла из формы
            file=request.FILES["file"]
            # вытаскиваем поле "title" из формы
            title = request.POST["title"]
            # если поле "title" не задано
            if not title:
                # имя фала остаеться изначальным
                title=file.name
            # записываем файл на диск
            write_file(file, title)
            # отправляем сообщение что файл импортирован
            messages.success(request, "Импорт завершен успешно")
        else:
            # форма не верна, отправляем сообщение об ошибке
            messages.error(request, "Импорт завершен неудачно")
    else:
        # запрос был не "POST" отправляем сообщение с ошибкой
        messages.warning(request, "Неверный формат запроса")

    # создаем ответ с редиректом на главную страницу
    response = HttpResponseRedirect(  # создаем редирект
        reverse(
            # имя редиреакта из "urls.py"
            "index"
        )
    )
    # устанавливаем в куки что это вторая вкладка
    response.set_cookie(COOKIE_ACTIVE_TAB, 1)
    return response


# вьбшка для скачивания файла
# нет своей страницы, просто качает файл
def download(request, filename):
    # создаем ответ с данными файла
    response = FileResponse(read_file(filename))
    # устанавливаем тип ответа "octet-stream" чтобы браузер качал файл а не открыл как страницу
    response['Content-Type'] = 'application/octet-stream'
    # устанавливаем имя файла
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


# вьбшка для удаления файла
# нет свое страницы, просто редирект на главную
def delete(request, filename):
    # удалям файл
    delete_file(filename)
    # создаем редирект
    response = HttpResponseRedirect(  # создаем редирект
        reverse(
            # имя редиреакта из "urls.py"
            "index"
        )
    )
    # устанавливаем в куки что это третья вкладка
    response.set_cookie(COOKIE_ACTIVE_TAB, 2)
    return response