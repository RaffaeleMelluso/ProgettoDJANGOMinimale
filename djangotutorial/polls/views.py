from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def article_list(request):
    articles = Article.objects.all()
    return render(request, "polls/article_list.html", {"articles": articles})