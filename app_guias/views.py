from django.shortcuts import render,redirect
from datetime import datetime

from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView

#from app_guias.forms import CursoFormulario
from app_guias.models import Agentes,Usuarios,Cargas

class AgentesListView(ListView):
    model = Agentes
    template_name = 'app_guias/lista_agentes.html'
    
class AgentesDeleteView(DeleteView):
    model = Agentes
    success_url = reverse_lazy ('Agentes')
    
class AgentesDetailView(DetailView):
    model = Agentes
    success_url = reverse_lazy ('Agentes')


class AgentesUpdateView(UpdateView):
    model  = Agentes
    fields = ('nombre_fwr', 'abrev_fwr','cotizador_fwr', 'manager_fwr','operativo_fwe','ctc_fwr')
    success_url = reverse_lazy ('Agentes')
    
class AgentesCreateView(CreateView):
    model  = Agentes
    fields = ('nombre_fwr', 'abrev_fwr','cotizador_fwr', 'manager_fwr','operativo_fwe','ctc_fwr')
    success_url = reverse_lazy ('Agentes')
    
def buscar_agente (request):
    if request.method == "POST":
        data = request.POST
        busqueda = data ["busqueda"]
        agente = Agentes.objects.filter(abrev_fwr__contains = busqueda)
        contexto = {
            "object_list" : agente,
        }
    http_responde=render(
            request = request,
            template_name= "app_guias/lista_agentes.html",
            context = contexto
        )
    return http_responde 




class UsuariosListView(ListView):
    model = Usuarios
    template_name = 'app_guias/lista_usuarios.html'
    
class UsuariosDeleteView(DeleteView):
    model = Usuarios
    success_url = reverse_lazy ('Usuarios')
    
class UsuariosDetailView(DetailView):
    model = Usuarios
    success_url = reverse_lazy ('Usuarios')
    
class UsuariosUpdateView(UpdateView):
    model  = Usuarios
    fields = ('nombre', 'apellido','area', 'email','telefono')
    success_url = reverse_lazy ('Usuarios')
    
class UsuariosCreateView(CreateView):
    model  = Usuarios
    fields = ('nombre', 'apellido','area', 'email','telefono')
    success_url = reverse_lazy ('Usuarios')


def buscar_usuario (request):
    if request.method == "POST":
        data = request.POST
        busqueda = data ["busqueda"]
        usuarios = Usuarios.objects.filter(area__contains = busqueda)
        contexto = {
            "object_list" : usuarios,
        }
    http_responde=render(
            request = request,
            template_name= "app_guias/lista_usuarios.html",
            context = contexto
        )
    return http_responde 


class GuiasListView(ListView):
    model = Cargas
    template_name = 'app_guias/lista_guias.html'
    
class GuiasDeleteView(DeleteView):
    model = Cargas
    success_url = reverse_lazy ('Guias')
    
class GuiasDetailView(DetailView):
    model = Cargas
    success_url = reverse_lazy ('Guias')
    
class GuiasUpdateView(UpdateView):
    model  = Cargas
    fields = ('ot', 'area','abrev_fwr', 'mawb','hawb','incoterm','cotizacion','bultos','peso','volumen','atd','ata','estado','retiro')
    success_url = reverse_lazy ('Guias')
    
class GuiasCreateView(CreateView):
    model  = Cargas
    fields = ('ot', 'area','abrev_fwr', 'mawb','hawb','incoterm','cotizacion','bultos','peso','volumen','atd','ata','estado','retiro')
    success_url = reverse_lazy ('Guias')


def buscar_guias (request):
    if request.method == "POST":
        data = request.POST
        busqueda = data ["busqueda"]
        cargas = Cargas.objects.filter(abrev_fwr__contains = busqueda)
        contexto = {
            "object_list" : cargas,
        }
    http_responde=render(
            request = request,
            template_name= "app_guias/lista_guias.html",
            context = contexto
        )
    return http_responde 
