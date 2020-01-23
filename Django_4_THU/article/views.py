from django.shortcuts import render
from article.models import Article


def list_article(request):
    articles = Article.objects.all()
    data={
        'articles': articles
    }
    return render(request, 'list_article.html', data)