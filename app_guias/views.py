from django.shortcuts import render,redirect
from datetime import datetime

from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView

#from app_guias.forms import CursoFormulario
from app_guias.models import Agentes,Usuarios,Cargas

class UsuariosListView(ListView):
    model = Usuarios
    template_name = 'app_guias/lista_usuarios.html'

# Create your views here.
def listar_agentes(request):
    contexto = {
        "agentes": Agentes.objects.all(),
    }
    http_responde = render(
        request=request,
        template_name='app_guias/lista_agentes.html',
        context=contexto,
    )
    return http_responde