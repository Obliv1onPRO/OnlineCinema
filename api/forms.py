from django import forms

class RegistationForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder' : 'Ник'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder' : 'Email'}))
    password = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'type': 'password', 'placeholder' : 'Пароль'}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder' : 'Ник'}))
    password = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'type': 'password', 'placeholder' : 'Пароль'}))


class RoomCreationForm(forms.Form):
    name = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={'placeholder' : 'Название'}))
    is_private = forms.BooleanField(required=True)
    iframe = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(attrs={'placeholder' : '...'}))
