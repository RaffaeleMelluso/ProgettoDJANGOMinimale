from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Article

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

    class Media:
        js = [
            "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js",
            "/static/js/mathjax_config.js",  # Configurazione personalizzata di MathJax
        ]
        css = {
            "all": ("admin/css/custom_admin.css",)  # Aggiungi CSS personalizzato se necessario
        }

# Registra il modello con la configurazione personalizzata
admin.site.register(Article, ArticleAdmin)