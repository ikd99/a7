from django.db.models import fields
from .models import requests, user_info
from django import forms
...

class PostAdd(forms.ModelForm):
    class Meta:
        model = requests
        fields = ['title', 'share_or_not', 'text', 'departure_place', 'destination_place', 'delivery_date', 'asking_price']
        labels={
            'title':"タイトル",
            'departure_place':"出発地",
            'destination_place':"目的地",
            'delivery_date':"配達希望日",
            'asking_price':"希望価格(円)",
            'text':"詳細"
        }

class TestForm(forms.Form):
    text = forms.CharField(label='文字入力')


class UserForm(forms.ModelForm):
    class Meta:
        model = user_info
        fields = ('is_driver', 'region')