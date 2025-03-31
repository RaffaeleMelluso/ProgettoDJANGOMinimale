from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import TestoDiProva
from django.conf import settings

class TestoDiProvaAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'render_contenuto')

    def render_contenuto(self, obj):
        # Usa MathJax per il rendering delle formule
        return mark_safe(f"""
            <div>{obj.contenuto}</div>
            <script type="text/javascript" async
                src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
            </script>
            
        """)

    render_contenuto.short_description = "Contenuto (renderizzato)"

    class Media:
        js = (
                "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js",
                settings.STATIC_URL + 'polls/matjax_promise.js'
            )

# Registra il modello con la configurazione personalizzata
admin.site.register(TestoDiProva, TestoDiProvaAdmin)