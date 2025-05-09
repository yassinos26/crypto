from django import forms

class EncryptForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label="Message à chiffrer")

class DecryptForm(forms.Form):
    encrypted_message = forms.CharField(widget=forms.Textarea, label="Message chiffré")
    key = forms.CharField(widget=forms.TextInput, label="Clé")