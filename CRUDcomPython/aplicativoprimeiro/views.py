from django.shortcuts import render
from aplicativoprimeiro.forms import CarrosForms

# Create your views here.

def home(request):
    return render(request, 'index.html')

def forms(request):
    data = {}
    data['forms'] =CarrosForms()
    return render(request, 'forms.html', data)