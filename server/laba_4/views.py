from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import UploadFileForm
from .file_utils import handle_uploaded_file


# пример простейшей вьющки
def hello_world(request):
    # простейший вывод html страницы
    return HttpResponse("Hello, world!")


def index(request):
    context = {
        "name": "laba_4",
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

    return HttpResponseRedirect(  # создаем редирект
        reverse(
            # имя редиреакта из "urls.py"
            "index"
        )
    )
