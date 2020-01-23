from django.urls import path
from article.views import list_article

urlpatterns=[
    path('', list_article, name='list_article'),
]