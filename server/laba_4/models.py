from django.db import models


# модель для экспорта файла
class ExportFile(models.Model):
    # поле имени
    title = models.CharField(max_length=50)
    #  поле даты создания файла на сервере 
    created_at = models.DateField()
    #  полное имя файла (нужно для скачивания)
    filename = models.CharField(max_length=255)

    # метод для создания нового эеземпляра модели с передачей нужных полей
    @classmethod
    def create(cls, title, filename, created_at):
        return cls(
            title=title,
            filename=filename,
            created_at=created_at,
        )
