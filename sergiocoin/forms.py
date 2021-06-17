from django.forms import ModelForm
from sergiocoin.models import Pessoa

# Create the form class.
class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'escolaridade','idade']