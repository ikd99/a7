from django.urls import path
from . import views

app_name='main'
urlpatterns = [
  path('', views.index, name='index'),
  path('post/', views.post, name='post'),
  path('detail/<int:num>', views.detail, name='detail'),
  path('log/', views.log, name='log'),
  path('mypage/', views.mypage, name='mypage'),
  path('profile/', views.profile, name='profile'),
  path('chat/<int:num>', views.chat, name='chat'),

  path('message', views.message, name='message'),
  path('detail/<int:num>', views.detail, name='detail'),
  path('evaluation/<int:num>', views.evaluation, name='evaluation'),
  path('request_complete/<int:num>', views.request_complete, name='request_complete'),

  path("payment/<int:num>", views.payment, name = "payment"),
  path('request_complete/<int:num>', views.request_complete, name='request_complete'),
  path('message', views.message, name='message'),

  # ↓以下使っていません
  # path('favorites/', views.favorites, name='favorites'),
]