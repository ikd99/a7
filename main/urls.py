from django.urls import path
from . import views

app_name='main'
urlpatterns = [
  path('', views.index, name='index'),
  path('post/', views.post, name='post'),
  path('mypage/', views.mypage, name='mypage'),
  path('profile/', views.profile, name='profile'),
  path('chat/<int:num>', views.chat, name='chat'),
]