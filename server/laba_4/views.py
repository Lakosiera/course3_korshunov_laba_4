from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import UploadFileForm
from .file_utils import handle_uploaded_file, read_dir

COOKIE_ACTIVE_TAB="active_tab"

# пример простейшей вьющки
def hello_world(request):
    # простейший вывод html страницы
    return HttpResponse("Hello, world!")


def index(request):
    files = read_dir()
    tab_index = request.COOKIES.get(COOKIE_ACTIVE_TAB, "0")
    context = {
        "name": "laba_4",
        "files": files,
        "tab_index": tab_index,
    }
    # ренедр вьюшки в html страницу
    return render(request, "index.html", context)


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file=request.FILES["file"]
            title = request.POST["title"]
            if not title:
                title=file.name
            handle_uploaded_file(file, title)
            messages.success(request, "Импорт завершен успешно")
        else:
            messages.error(request, "Импорт завершен неудачно")
    else:
        messages.warning(request, "Неверный формат запроса")


    response = HttpResponseRedirect(  # создаем редирект
        reverse(
            # имя редиреакта из "urls.py"
            "index"
        )
    )
    response.set_cookie(COOKIE_ACTIVE_TAB, 1)
    return response
