from datetime import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse 

def saludar(request):
    saludo = "Bienvanido al sistema de cargas"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def inicio (request):
    contexto = {}
    
    http_responde= render(
        request=request,
        template_name= 'app_guias/index.html',
        context = contexto,
    )
    return http_responde

def ayuda (request):
    contexto = {}
    
    http_responde= render(
        request=request,
        template_name= 'app_guias/ayuda.html',
        context = contexto,
    )
    return http_responde
