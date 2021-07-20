from django import forms

class PassagemForm(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    ida = forms.DateField(label='Data de partida')
    volta = forms.DateField(label='Data de volta')
