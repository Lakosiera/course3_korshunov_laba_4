from django.db import models


class ExportFile(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateField()
    filename = models.CharField(max_length=255)

    @classmethod
    def create(cls, title, filename, created_at):
        book = cls(
            title=title,
            filename=filename,
            created_at=created_at,
        )
        return book
