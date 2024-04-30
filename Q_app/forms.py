from django import forms


class fpForm(forms.Form):
    mail= forms.CharField(max_length=50)
    password= forms.CharField(max_length=50,widget=forms.TextInput(attrs={'id':'password1'}))
    confirm_password= forms.CharField(max_length=50,widget=forms.TextInput(attrs={'id':'password2'}))