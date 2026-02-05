from django import forms
"""
Two type of forms are there in django:
1. Form => we must define every custom field
2. ModelForm => django automatically define the forms on the basis of model
"""

"""Form"""
class LoginForm(forms.Form):
    email = forms.EmailField(label='User-Email')
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(), label='User-Password')
    is_admin = forms.BooleanField()