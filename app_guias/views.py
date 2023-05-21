from django.shortcuts import render,redirect
from datetime import datetime

from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView

#from app_guias.forms import CursoFormulario
from app_guias.models import Agentes,Usuarios,Cargas



class UsuariosListView(ListView):
    model = Usuarios
    template_name = 'app_guias/lista_usuarios.html'

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