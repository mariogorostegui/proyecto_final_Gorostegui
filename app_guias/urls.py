from django.contrib import admin
from django.urls import path


from app_guias.views import AgentesListView,AgentesDetailView,AgentesUpdateView,AgentesDeleteView,AgentesCreateView, \
    buscar_agente, \
    UsuariosCreateView,UsuariosDeleteView,UsuariosDetailView,UsuariosListView,UsuariosUpdateView, buscar_usuario, \
    GuiasCreateView,GuiasDeleteView,GuiasDetailView,GuiasListView,GuiasUpdateView, buscar_guias


urlpatterns = [
 
    path("lst_agentes/",AgentesListView.as_view(),name = "Agentes"),
    path("detalle_agente/<int:pk>/",AgentesDetailView.as_view(),name = "detalle_agente"),
    path("actualiza_agente/<int:pk>/",AgentesUpdateView.as_view(),name = "actualiza_agente"),
    path("elimina_agente/<int:pk>/",AgentesDeleteView.as_view(),name = "borra_agente"),
    path("crear_agente/",AgentesCreateView,name = "crear_agente"),
    path("buscar_agente/",buscar_agente,name='buscar_agente'),
   
   
    path ("usuarios/",UsuariosListView.as_view(),name="Usuarios"), 
    path("detalle_usuario/<int:pk>/",UsuariosDetailView.as_view(),name = "detalle_usuario"),
    path("actualiza_usuario/<int:pk>/",UsuariosUpdateView.as_view(),name = "actualiza_usuario"),
    path("elimina_usuario/<int:pk>/",UsuariosDeleteView.as_view(),name = "borra_usuario"),
    path("crear_usuario/",UsuariosCreateView,name = "crear_usuario"),
    path("buscar_usuario/",buscar_usuario,name='buscar_usuario'),
    
    path ("guias/",GuiasListView.as_view(),name="Guias"), 
    path("detalle_guia/<int:pk>/",GuiasDetailView.as_view(),name = "detalle_guia"),
    path("actualiza_guia/<int:pk>/",GuiasUpdateView.as_view(),name = "actualiza_guia"),
    path("elimina_guia/<int:pk>/",GuiasDeleteView.as_view(),name = "elimina_guia"),
    path("crear_guia/",GuiasCreateView,name = "crear_guia"),
    path("buscar_guia/",buscar_guias,name='buscar_guias'),

    
]
