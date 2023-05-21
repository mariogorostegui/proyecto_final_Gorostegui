from django.contrib import admin
from django.urls import path


from app_guias.views import AgentesListView,UsuariosListView,AgentesDetailView,AgentesUpdateView,AgentesDeleteView,AgentesCreateView, \
    buscar_agente, \
    UsuariosCreateView,UsuariosDeleteView,UsuariosDetailView,UsuariosListView,UsuariosUpdateView, buscar_usuario


urlpatterns = [
 
    path("lst_agentes/",AgentesListView.as_view(),name = "Agentes"),
    path("detalle_agente/<int:pk>/",AgentesDetailView.as_view(),name = "detalle_agente"),
    path("actualiza_agente/<int:pk>/",AgentesUpdateView.as_view(),name = "actualiza_agente"),
    path("elimina_agente/<int:pk>/",AgentesDeleteView.as_view(),name = "borra_agente"),
    path("crear_agente/",AgentesCreateView.as_view(),name = "crear_agente"),
    path("buscar_agente/",buscar_agente,name='buscar_agente'),
   
   
    path ("usuarios/",UsuariosListView.as_view(),name="Usuarios"), 
    path("detalle_usuario/<int:pk>/",UsuariosDetailView.as_view(),name = "detalle_usuario"),
    path("actualiza_usuario/<int:pk>/",UsuariosUpdateView.as_view(),name = "actualiza_usuario"),
    path("elimina_usuario/<int:pk>/",UsuariosDeleteView.as_view(),name = "borra_usuario"),
    path("crear_usuario/",UsuariosCreateView.as_view(),name = "crear_usuario"),
    path("buscar_usuario/",buscar_usuario,name='buscar_usuario')
    
    

    
]
