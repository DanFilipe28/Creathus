from django.shortcuts import render, redirect
from sergiocoin.forms import PessoaForm
from sergiocoin.models import Pessoa


# Create your views here.
def home(request):
    return render(request, 'index.html')


def form(request):
    data = {}
    data["form"] = PessoaForm()
    return render(request, 'form.html', data)


def create(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Pessoa.objects.get(pk=pk)
    return render(request, 'view.html', data)
