from .models import requests
from django import forms
...

class PostForm(forms.Form):
    title = forms.CharField(label='タイトル')
    text = forms.CharField(label='詳細', widget=forms.Textarea)
    departure_place = forms.CharField(label='出発地')
    destination_place  = forms.CharField(label='目的地')
    delivery_date = forms.DateField(label='配達希望日')
    asking_price = forms.IntegerField(label='希望価格（日）')
    
class TestForm(forms.Form):
    text = forms.CharField(label='文字入力')