from django.urls import path
from . import views

app_name='main'
urlpatterns = [
  path('', views.index, name='index'),
  path('post/', views.post, name='post'),
  path('mypage/', views.getMyPage, name='mypage'),
  path('chat/', views.chat, name='chat'),
]