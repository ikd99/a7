from django import forms

#フォームクラス作成
class login_form(forms.Form):
  user_name = forms.CharField(max_length=20, required = True)
  hashed_pass = forms.IntegerField(required = True)
