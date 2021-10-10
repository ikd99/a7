from django.urls import path
from . import views

app_name='main'
urlpatterns = [
  path('', views.top_share, name='top_share'),
  path('chat/', views.chat, name='chat'),
]