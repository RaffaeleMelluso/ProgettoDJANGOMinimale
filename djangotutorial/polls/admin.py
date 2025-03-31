from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import TestoDiProva

class TestoDiProvaAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'render_contenuto')

    def render_contenuto(self, obj):
        # Usa MathJax per il rendering delle formule
        return mark_safe(f"""
            <div>{obj.contenuto}</div>
            <script type="text/javascript" async
                src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
            </script>
            <script>
                MathJax.typesetPromise();  // Forza MathJax a eseguire il rendering
            </script>
        """)

    render_contenuto.short_description = "Contenuto (renderizzato)"

# Registra il modello con la configurazione personalizzata
admin.site.register(TestoDiProva, TestoDiProvaAdmin)