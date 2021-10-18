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

class PostForm(forms.Form):
    title = forms.CharField(label='タイトル')
    text = forms.CharField(label='詳細', widget=forms.Textarea)
    departure_place = forms.CharField(label='出発地')
    destination_place  = forms.CharField(label='目的地')
    delivery_date = forms.DateField(label='配達希望日')
    asking_price = forms.IntegerField(label='希望価格（日）')
    
class TestForm(forms.Form):
    text = forms.CharField(label='文字入力')


class UserForm(forms.Form):
    is_driver = forms.BooleanField(label='ドライバー登録', required=True)
    region = forms.CharField(label='地域（例：〇〇県〇市）', required=True)

def wrap_boolean_check(v):
    return not (v is False or v is None or v == '' or v == 0)

class StatusForm(forms.Form):
    check = forms.BooleanField(
        initial=1,
        widget=forms.CheckboxInput(check_test=wrap_boolean_check)
    )
