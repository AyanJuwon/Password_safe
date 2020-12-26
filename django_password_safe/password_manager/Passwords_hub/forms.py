from .models import PasswordList
from django import forms
class PasswordForm(forms.ModelForm):
    
    class Meta:
        
        model = PasswordList
        fields = ("password_name","password_username","password")
