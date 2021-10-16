from django.urls import path
from . import views

app_name='main'
urlpatterns = [
  path('', views.index, name='index'),
  path('post/', views.post, name='post'),
  path('mypage/', views.getMyPage, name='mypage'),
  path('chat/<int:num>', views.chat, name='chat'),
  path('detail/<int:num>', views.detail, name='detail'),
  path('history/', views.history, name='history'),
  path('favorites/', views.favorites, name='favorites'),
  path('match_complete/', views.match_complete, name='match_complete'),
]