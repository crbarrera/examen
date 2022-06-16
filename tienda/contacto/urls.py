
from django import urls
from django.urls import path, include
from . import views
 
urlpatterns = [
 
    # listar los mensajes de la bd
    path('listar_mensajes', views.listar_mensajes, name="listar_mensajes"),
    
    # agregar un mensaje    
    path('agregar_mensaje', views.agregar_mensaje, name="agregar_mensaje"),
 
    # editar un mensaje
    path('editar_mensaje/<int:mensaje_id>', views.editar_mensaje ,name="editar_mensaje"),
 
    # borrar un mensaje
    path('borrar_mensaje/<int:mensaje_id>', views.borrar_mensaje, name="borrar_mensaje"),
    
    # llamando a las clases 
    path('add_mensaje', views.MensajeCreate.as_view(), name="add_mensaje"),
 
    path('list_mensajes/', views.MensajeList.as_view(), name='list_mensajes'),
 
    path('edit_mensaje/<int:pk>', views.MensajeUpdate.as_view(), name='edit_mensaje'),
 
    path('del_mensaje/<int:pk>', views.MensajeDelete.as_view(), name='del_mensaje'),
    
    # path(r'^about$', views.about, name='about'),
    
    # path(r'^index$', views.index, name='index'),
    
    path('index/', views.index, name='index'),
 
]


