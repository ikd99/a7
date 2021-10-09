from .models import requests
from django import forms
...

class PostAdd(forms.ModelForm):
    class Meta:
        model = requests
        fields = ['title', 'share_or_not', 'text', 'departure_place', 'destination_place', 'delivery_date', 'asking_price']
        labels={
            'title':"タイトル",
            'text':"内容",
            'departure_place':"出発地",
            'destination_place':"目的地",
            'delivery_date':"配達日",
            'asking_price':"希望価格(円)"
        }