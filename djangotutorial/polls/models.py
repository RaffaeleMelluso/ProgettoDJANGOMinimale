from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class TestoDiProva(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = CKEditor5Field('Text', config_name='extends')

    def __str__(self):
        return self.titolo