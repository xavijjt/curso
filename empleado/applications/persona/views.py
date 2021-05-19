from applications.departamento import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView)
from .models import Empleado


class InicioView(TemplateView):
    """vista que carga la paginas de inicio """
    template_name = 'inicio.html'

class ListAllEmpleados ( ListView):
    template_name = 'persona/list_all.html'
    paginate_by=4
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        print("***********")
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )
        print("****" , lista)
        return lista


class ListaEmpleadosAdmin( ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by=10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
    

class ListByAreaEmpleado (ListView):
    template_name = 'persona/lis_by_area.html'
    context_object_name = 'empleados' 
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area
        )
        return lista
    
class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print("***********")
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        print("****" , lista)
        return lista

class ListHabilidadesEmpleado (ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=3)
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'

    def get_context_data(self,**kwargs):
        context = super(EmpleadoDetailView,self).get_context_data(**kwargs)
        context['titulo']='Empleado del mes'
        return context

class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    fields = ['first_name',
        'lest_name',
        'job',
        'departamento',
        'habilidades'
        ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self,form):
        empleado = form.save(commit = False)
        empleado.full_name = empleado.first_name + ' ' + empleado.lest_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)

class SuccesView(TemplateView):
    template_name = 'persona/success.html'

class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields =[
        'first_name',
        'lest_name',
        'job',
        'departamento',
        'habilidades'
    ]
    
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self,request,*args,**kwargs):
        self.objects = self.get_object()
        print ('***METODO POST****')
        print('****************')
        print (request.POST)
        print(request.POST['lest_name'])
        return super().post(request,*args,**kwargs)

class EmpleadoDeleteView(DeleteView):
    model=Empleado
    template_name='persona/delete.html'
    success_url = reverse_lazy('persona_app:empleados_admin')

    