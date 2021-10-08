from .models import request  # importに追加
from django import forms
...

class PostAdd(forms.ModelForm):
    class Meta:
        model = request
        fields = ['title', 'share_or_not', 'text', 'departure_place', 'destination_place', 'delivery_date', 'asking_price']