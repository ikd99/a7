from django.urls import path
from . import views

app_name='main'
urlpatterns = [
  path('', views.index, name='index'),
  path('post/', views.post, name='post'),
  path('mypage/', views.getMyPage, name='mypage'),
  path('top_share/', views.top_share, name='top_share'),
  path('chat/<int:num>', views.chat, name='chat'),
]