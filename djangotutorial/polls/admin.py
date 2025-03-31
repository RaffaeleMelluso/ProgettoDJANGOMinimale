from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Article  # Assicurati di importare il modello corretto

class ArticleAdminForm(forms.ModelForm):
    """Form personalizzato per il modello Article con CKEditor5Widget."""

    class Meta:
        model = Article
        fields = "__all__"
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ("title",)

# Registra il modello con la configurazione personalizzata
admin.site.register(Article, ArticleAdmin)