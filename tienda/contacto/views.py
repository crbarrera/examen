from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from contacto.models import Mensaje
from .forms import MensajeForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MensajeSerializer
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

def listar_mensajes(request):
    mensajes = Mensaje.objects.all()
    return render(request, "contacto/listar_mensajes.html", {'mensajes': mensajes})

def agregar_mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_mensaje")
    else:
        form = MensajeForm()
        return render(request, "contacto/agregar_mensaje.html", {'form': form})
 
def borrar_mensaje(request, mensaje_id):
    instancia = Mensaje.objects.get(id=mensaje_id)
    instancia.delete()
 
    return redirect('list_mensajes')
 
def editar_mensaje(request, mensaje_id):
    instancia = Mensaje.objects.get(id=mensaje_id)
 
    form = MensajeForm(instance=instancia)
 
    if request.method == "POST":
        form = MensajeForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
 
    return render(request, "contacto/editar_mensaje.html", {'form': form})

# --Otra forma usando clases Generics -------
class MensajeCreate(CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'contacto/mensaje_form.html'
    success_url = reverse_lazy("list_mensajes")
    
class MensajeList(ListView):
    model = Mensaje
    template_name = 'contacto/list_mensajes.html'
    # paginate_by = 4
 
class MensajeUpdate(UpdateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'contacto/mensaje_form.html'
    success_url = reverse_lazy('list_mensajes')
 
        
 
class MensajeDelete(DeleteView):
    model = Mensaje
    template_name = 'contacto/mensaje_delete.html'
    success_url = reverse_lazy('list_mensajes')
    
    
def index(request):
    return render(request,'index.html')

# El decorador @api_view verifica que la solicitud HTTP apropiada 
# se pase a la función de vista. En este momento, solo admitimos solicitudes GET
@api_view(['GET'])
def mensaje_collection(request):
    if request.method == 'GET':
        mensajes = Mensaje.objects.all()
        serializer = MensajeSerializer(mensajes, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'PUT', 'DELETE'])
def mensaje_element(request, pk):
    mensaje = get_object_or_404(Mensaje, id=pk)
 
    if request.method == 'GET':
        serializer = MensajeSerializer(mensaje)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        mensaje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        mensaje_new = JSONParser().parse(request) 
        serializer = MensajeSerializer(mensaje, data=mensaje_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'POST'])
def mensaje_collection(request):
    if request.method == 'GET':
        mensajes = Mensaje.objects.all()
        serializer = MensajeSerializer(mensajes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


