from django.contrib import admin
from django.urls import path


from app_guias.views import AgentesListView,UsuariosListView,AgentesDetailView,AgentesUpdateView,AgentesDeleteView,AgentesCreateView, \
    buscar_agente


urlpatterns = [
 
    path("lst_agentes/",AgentesListView.as_view(),name = "Agentes"),
    path("detalle_agente/<int:pk>/",AgentesDetailView.as_view(),name = "detalle_agente"),
    path("actualiza_agente/<int:pk>/",AgentesUpdateView.as_view(),name = "actualiza_agente"),
    path("elimina_agente/<int:pk>/",AgentesDeleteView.as_view(),name = "borra_agente"),
    path("crear_agente/",AgentesCreateView.as_view(),name = "crear_agente"),
    path("buscar_agente/",buscar_agente,name='buscar_agente'),
    
    path ("usuarios/",UsuariosListView.as_view(),name="Usuarios"),

    
]
