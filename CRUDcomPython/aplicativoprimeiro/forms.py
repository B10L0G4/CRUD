from django. forms import ModelForm
from aplicativoprimeiro.forms import Carros
class CarrosForms(ModelForm):
    class Meta:
        model = Carros
        fields = ['Modelo', 'Marca', 'Ano']