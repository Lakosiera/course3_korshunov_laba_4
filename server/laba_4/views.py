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
            handle_uploaded_file(request.FILES["file"])
            messages.success(request, "Импорт завершен успешно")
            # return HttpResponseRedirect("/success/url/")
            return HttpResponseRedirect(  # создаем редирект
                reverse(
                    # имя редиреакта из "urls.py"
                    "index"
                )
            )
        else:
            messages.error(request, "Импорт завершен неудачно")
            return HttpResponseRedirect(  # создаем редирект
                reverse(
                    # имя редиреакта из "urls.py"
                    "index"
                )
            )
    else:
        messages.warning(request, "Неверный формат запроса")

    return HttpResponseRedirect(  # создаем редирект
        reverse(
            # имя редиреакта из "urls.py"
            "index"
        )
    )
