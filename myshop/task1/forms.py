from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(label='Введите логин', max_length=100)
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    age = forms.IntegerField(label='Введите свой возраст')
