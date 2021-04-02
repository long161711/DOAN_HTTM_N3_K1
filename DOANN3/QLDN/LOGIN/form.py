from django import forms
from .models import user

class contact_Form(forms.ModelForm):
    class Meta:
        model = user
        fields = ['email', 'password']