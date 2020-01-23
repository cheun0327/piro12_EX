from django.shortcuts import render
from article.models import Article


def list_article(request):
    articles = Article.objects.all()
    data={
        'articles': articles
    }
    return render(request, 'list_article.html', data)

def detail_article(request, pk):
    article=Article.objects.get(pk=pk)
    data={
        'article': article
    }
    return render(request, 'detail_article.html', data)

def create_article(request):
    return render(request, 'create_article.html')