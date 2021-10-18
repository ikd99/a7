from django.urls import path
from . import views

app_name='main'
urlpatterns = [
  path('', views.index, name='index'),
  path('post/', views.post, name='post'),
  path('mypage/', views.mypage, name='mypage'),
  path('profile/', views.profile, name='profile'),
  path('chat/<int:num>', views.chat, name='chat'),
  path('message', views.message, name='message'),
  path('detail/<int:num>', views.detail, name='detail'),
  path('evaluation/<int:num>', views.evaluation, name='evaluation'),
  path('request_complete/<int:num>', views.request_complete, name='request_complete'),
  path("payment/<int:num>", views.payment, name = "payment"),
  path('log/', views.log, name='log'),

  # ↓以下使っていません
  # path('log_before/', views.log_before, name='log_before'),
  # path('history/', views.history, name='history'),
  # path('match_complete/', views.match_complete, name='match_complete'),
  # path('favorites/', views.favorites, name='favorites'),
  # path('done_post/', views.done_post, name='done_post'),
]