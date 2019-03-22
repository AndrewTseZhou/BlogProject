from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('archives/', views.archives, name='archives'),
    path('article_detail/', views.article_detail, name='article_detail'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('category/', views.category, name='category'),
    path('comment/post/', views.comment_post, name='comment_post'),
]
