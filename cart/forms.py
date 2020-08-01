from django import forms

QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class AddProduct(forms.Form):
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)