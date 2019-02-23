from django import forms

class RegistationForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder' : 'Ник'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder' : 'Email'}))
    password = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'type': 'password', 'placeholder' : 'Пароль'}))

