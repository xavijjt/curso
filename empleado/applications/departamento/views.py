from django.shortcuts import render
#from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Departamento
# Create your views here.


class DepartamentoListView(ListView):
    template_name = 'departamento/lista.html'
    model = Departamento
    context_object_name = 'departamentos'