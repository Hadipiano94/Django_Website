from django import forms


class CreateNewTel(forms.Form):
    name = forms.CharField(label="Name", max_length=128)
    tel = forms.CharField(label="Tel", max_length=65)
    dnt_call = forms.BooleanField(label="Don't call", required=False)
