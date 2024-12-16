from django import forms


# класс для формы импорта файла
class ImportFileForm(forms.Form):
    # опциональное поле для нового имени файла
    title = forms.CharField(max_length=50, required=False)
    # поле для бинарных данных файла
    file = forms.FileField()
