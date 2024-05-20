# forms.py
from django import forms

class EmailForm(forms.Form):
    sender = forms.CharField(label='Váš e-mail', max_length=100)
    subject = forms.CharField(label='Předmět', max_length=100)
    message = forms.CharField(label='Obsah zprávy', widget=forms.Textarea)