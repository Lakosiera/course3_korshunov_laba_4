from django import forms


# класс для формы импорта файла
class ImportFileForm(forms.Form):
    # опциональное поле для нового имени файла
    filename = forms.CharField(max_length=50, required=False)
    # поле для бинарных данных файла
    file = forms.FileField()


# класс для формы данных музыкального альбома
# TODO https://en.wikipedia.org/wiki/Album
class MusicAlbumForm(forms.Form):
    filename = forms.CharField(max_length=50, required=True)
    title = forms.CharField(max_length=50, required=True)
    relesased_at = forms.CharField(max_length=50, required=True)
    length = forms.IntegerField(min_value=1, required=True)
    artist = forms.CharField(max_length=50, required=False)
    genre = forms.CharField(max_length=50, required=False)
    # Studio / Live / Solo
    type = forms.CharField(max_length=50, required=False)
