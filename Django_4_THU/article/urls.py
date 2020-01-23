from django.urls import path
from article.views import list_article, detail_article, create_article

urlpatterns=[
    path('', list_article, name='list_article'),
    path('detail/<int:pk>/', detail_article, name='detail_article'),
    path('create/', create_article, name='create_article')
]