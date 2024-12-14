from django.urls import path

from . import views

# пути для модуля 'laba_4'
urlpatterns = [
    # корневой путь (т.е. "/" или "http://localhost:8004/")
    path(
        route="",  # путь
        view=views.index,  # вьюшка из файла 'views.py'
        name="index",  # условное имя пути (можно неуказывать)
    ),
]
