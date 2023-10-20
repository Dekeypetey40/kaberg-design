from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)