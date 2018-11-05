from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('index/', views.index), 
    path('article/<int:article_id>/',views.article_page,name='article'),
    path('to_create_article/',views.to_create_article,name='to_create_article'),
    path('create_article/',views.create_article,name='create_article'),
    path('to_edit_article/<int:article_id>',views.to_edit_article,name='to_edit_article'),
    path('edit_article/',views.edit_article,name='edit_article'),
]
