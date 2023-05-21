from django.contrib import admin
from django.urls import path


from app_guias.views import listar_agentes,UsuariosListView


urlpatterns = [
 
    path('lst_agentes/',listar_agentes,name="Agentes"),
    
    path ("usuarios/",UsuariosListView.as_view(),name="Usuarios"),

    
]
