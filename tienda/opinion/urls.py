from django import urls
from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required
 
urlpatterns = [
 
    # listar los comentarios de la bd
    path('listar_comentarios', views.listar_comentarios, name="listar_comentarios"),
    
    # agregar un comentario    
    path('agregar_comentario', views.agregar_comentario, name="agregar_comentario"),
 
    # editar un comentario
    path('editar_comentario/<int:comentario_id>', views.editar_comentario ,name="editar_comentario"),
 
    # borrar un comentario
    path('borrar_comentario/<int:comentario_id>', login_required(views.borrar_comentario), name="borrar_comentario"),
    
    # llamando a las clases 
    path('add_comentario', login_required(views.ComentarioCreate.as_view()), name="add_comentario"),
 
    path('list_comentarios/', login_required(views.ComentarioList.as_view()), name='list_comentarios'),
 
    path('edit_comentario/<int:pk>', views.ComentarioUpdate.as_view(), name='edit_comentario'),
 
    path('del_comentario/<int:pk>', views.ComentarioDelete.as_view(), name='del_comentario'),
    
    # path(r'^about$', views.about, name='about'),
    
    # path(r'^index$', views.index, name='index'),
    
    path('index/', views.index, name='index'),
    
    # api
    path('comentarios/',  views.comentario_collection , name='comentario_collection'),
    path('comentarios/<int:pk>/', views.comentario_element ,name='comentario_element')
    
]
