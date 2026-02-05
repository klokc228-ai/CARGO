from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'telegram', 'cargo_type', 'additional_info']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'telegram': forms.TextInput(attrs={'placeholder': 'Telegram'}),
            'cargo_type': forms.TextInput(attrs={'placeholder': 'Тип груза'}),
            'additional_info': forms.Textarea(attrs={'placeholder': 'Дополнительная информация', 'rows': 3}),
        }
