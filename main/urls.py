from django.urls import path
from . import views

app_name='main'
urlpatterns = [
  path('chat/', views.chat, name='chat'),
]