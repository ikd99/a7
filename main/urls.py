from django.urls import path
from . import views

app_name='main'
urlpatterns = [
  path('index/', views.index, name='index'),
  path('post/', views.post, name='post'),
  path('mypage/', views.getMyPage, name='mypage'),
  path('', views.top_share, name='top_share'),
  path('chat/', views.chat, name='chat'),
]