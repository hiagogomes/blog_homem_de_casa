from django import forms
from .models import MensagemContato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 5}),
        }
