from .models import Convertor
from django.forms import ModelForm, TextInput

class ConvertorForm(ModelForm):
    class Meta:
        model = Convertor
        fields = ["number", "b", "c"]
        widgets = {
            "number": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your number"
            }),
            "b": TextInput(attrs={
                "class": "form-control",
                "placeholder": "your number system"
            }),
            "c": TextInput(attrs={
                "class": "form-control",
                "placeholder": "number system you want"
            }),
        }