from django.shortcuts import render,redirect
from datetime import datetime

from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView

from app_guias.forms import AgentesFormulario,UsuarioFormulario,CargasFormulario
from app_guias.models import Agentes,Usuarios,Cargas


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class AgentesListView(ListView):
    model = Agentes
    template_name = 'app_guias/lista_agentes.html'
    
class AgentesDeleteView(LoginRequiredMixin,DeleteView):
    model = Agentes
    success_url = reverse_lazy ('Agentes')
    
class AgentesDetailView(LoginRequiredMixin,DetailView):
    model = Agentes
    success_url = reverse_lazy ('Agentes')


class AgentesUpdateView(LoginRequiredMixin,UpdateView):
    model  = Agentes
    fields = ('nombre_fwr', 'abrev_fwr','cotizador_fwr', 'manager_fwr','operativo_fwe','ctc_fwr')
    success_url = reverse_lazy ('Agentes')

@login_required
def AgentesCreateView(request):
    
    if request.method== "POST":
        formulario = AgentesFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre_fwr = data["nombre_fwr"]
            abrev_fwr = data["abrev_fwr"]
            cotizador_fwr = data['cotizador_fwr']
            operativo_fwe = data['operativo_fwe']
            ctc_fwr = data ['ctc_fwr']
            creador = request.user
            agente = Agentes.objects.create(nombre_fwr=nombre_fwr,abrev_fwr=abrev_fwr,cotizador_fwr=cotizador_fwr,operativo_fwe=operativo_fwe,ctc_fwr=ctc_fwr,creador=creador)
            agente.save()
        
            url_exitosa = reverse ("Agentes")
            return redirect(url_exitosa)
    else:
        formulario = AgentesFormulario()
  
        http_responde=render(
            request = request,
            template_name= 'app_guias/formulario_agente.html',
            context = {'formulario':formulario}
        )
    return http_responde



@login_required   
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
            template_name= "app_guias/lista_agente.html",
            context = contexto
        )
    return http_responde 




class UsuariosListView(ListView):
    model = Usuarios
    template_name = 'app_guias/lista_usuarios.html'
    
class UsuariosDeleteView(LoginRequiredMixin,DeleteView):
    model = Usuarios
    success_url = reverse_lazy ('Usuarios')
    
class UsuariosDetailView(LoginRequiredMixin,DetailView):
    model = Usuarios
    success_url = reverse_lazy ('Usuarios')
    
class UsuariosUpdateView(LoginRequiredMixin,UpdateView):
    model  = Usuarios
    fields = ('nombre', 'apellido','area', 'email','telefono')
    success_url = reverse_lazy ('Usuarios')


@login_required   
def UsuariosCreateView(request):
    
    if request.method== "POST":
        formulario = UsuarioFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            area = data['area']
            email = data['email']
            telefono = data ['telefono']
            creador = request.user
            usuario = Usuarios.objects.create(nombre=nombre,apellido=apellido,area=area,email=email,telefono=telefono,creador=creador)
            usuario.save()
        
            url_exitosa = reverse ("Usuarios")
            return redirect(url_exitosa)
    else:
        formulario = UsuarioFormulario()
  
        http_responde=render(
            request = request,
            template_name= 'app_guias/formulario_usuario.html',
            context = {'formulario':formulario}
        )
    return http_responde

@login_required
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
    
class GuiasDeleteView(LoginRequiredMixin,DeleteView):
    model = Cargas
    success_url = reverse_lazy ('Guias')
    
class GuiasDetailView(LoginRequiredMixin,DetailView):
    model = Cargas
    success_url = reverse_lazy ('Guias')
    
class GuiasUpdateView(LoginRequiredMixin,UpdateView):
    model  = Cargas
    fields = ('ot', 'area','abrev_fwr', 'mawb','hawb','incoterm','cotizacion','bultos','peso','volumen','atd','ata','estado','retiro')
    success_url = reverse_lazy ('Guias')

@login_required   
def GuiasCreateView(request):
    if request.method== "POST":
        formulario = CargasFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            ot = data["ot"]
            mawb = data["mawb"]
            hawb = data['hawb']
            incoterm = data['incoterm']
            area = data ['area']
            abrev_fwr = data ['abrev_fwr']
            cotizacion = data ['cotizacion']
            bultos = data ['bultos']
            peso = data ['peso']
            volumen = data ['volumen']
            atd = data ['atd']
            ata = data ['ata']
            estado = data ['estado']
            retiro = data ['retiro']
            creador = request.user
            guia = Cargas.objects.create(ot=ot,mawb=mawb,hawb=hawb,incoterm=incoterm,area=area, \
                abrev_fwr=abrev_fwr,cotizacion=cotizacion,bultos=bultos,peso=peso,volumen=volumen,atd=atd,ata=ata, \
                estado=estado,retiro=retiro,creador=creador)
            guia.save()
        
            url_exitosa = reverse ("Guias")
            return redirect(url_exitosa)
    else:
        formulario = CargasFormulario()
  
        http_responde=render(
            request = request,
            template_name= 'app_guias/formulario_guia.html',
            context = {'formulario':formulario}
        )
    return http_responde

@login_required
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
