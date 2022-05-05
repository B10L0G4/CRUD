from django. forms import ModelForm
from aplicativoprimeiro.models import Carros
class CarrosForms(ModelForm):
    class Meta:
        model = Carros
        fields = ['Modelo', 'Marca', 'Ano']