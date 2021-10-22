from django.urls import path
from . import views

app_name='main'
urlpatterns = [
  path('', views.index, name='index'),
  path('post/', views.post, name='post'),
  path('detail/<int:num>', views.detail, name='detail'),
  path('log/', views.log, name='log'),
  path('profile/', views.profile, name='profile'),
  path('chat/<int:num>', views.chat, name='chat'),
  path('evaluation/<int:num>', views.evaluation, name='evaluation'),
  path('request_complete/<int:num>', views.request_complete, name='request_complete'),
  path("payment/<int:num>", views.payment, name = "payment"),

]