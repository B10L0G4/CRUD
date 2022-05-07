from django.shortcuts import render
from aplicativoprimeiro.forms import CarrosForms

# Create your views here.

def home(request):
    return render(request, 'index.html')

def forms(request):
    data = {}
    data['forms'] = CarrosForms()
    return render(request, 'forms.html', data)
def create(request):
    form= CarrosForms(request.POST or NONE)
    if form.is_valid():
        form(request).save()
        return redirect('home')