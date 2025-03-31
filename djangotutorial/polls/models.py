from django.db import models
from ckeditor.fields import RichTextField

class TestoDiProva(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = RichTextField()

    def __str__(self):
        return self.titolo