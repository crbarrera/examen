from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from opinion.models import Comentario
from .forms import ComentarioForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ComentarioSerializer
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

def listar_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, "opinion/listar_comentarios.html", {'comentarios': comentarios})

def agregar_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_comentario")
    else:
        form = ComentarioForm()
        return render(request, "opinion/agregar_comentario.html", {'form': form})
 
def borrar_comentario(request, comentario_id):
    instancia = Comentario.objects.get(id=comentario_id)
    instancia.delete()
 
    return redirect('list_comentarios')
 
def editar_comentario(request, comentario_id):
    instancia = Comentario.objects.get(id=comentario_id)
 
    form = ComentarioForm(instance=instancia)
 
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
 
    return render(request, "opinion/editar_comentario.html", {'form': form})

# --Otra forma usando clases Generics -------
class ComentarioCreate(CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'opinion/comentario_form.html'
    success_url = reverse_lazy("list_comentarios")
    
class ComentarioList(ListView):
    model = Comentario
    template_name = 'opinion/list_comentarios.html'
    # paginate_by = 4
 
class ComentarioUpdate(UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'opinion/comentario_form.html'
    success_url = reverse_lazy('list_comentarios')
 
        
 
class ComentarioDelete(DeleteView):
    model = Comentario
    template_name = 'opinion/comentario_delete.html'
    success_url = reverse_lazy('list_comentarios')
    
    
def index(request):
    return render(request,'index.html')

# El decorador @api_view verifica que la solicitud HTTP apropiada 
# se pase a la función de vista. En este momento, solo admitimos solicitudes GET
@api_view(['GET'])
def comentario_collection(request):
    if request.method == 'GET':
        comentarios = Comentario.objects.all()
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'PUT', 'DELETE'])
def comentario_element(request, pk):
    comentario = get_object_or_404(Comentario, id=pk)
 
    if request.method == 'GET':
        serializer = ComentarioSerializer(comentario)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comentario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        comentario_new = JSONParser().parse(request) 
        serializer = ComentarioSerializer(comentario, data=comentario_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'POST'])
def comentario_collection(request):
    if request.method == 'GET':
        comentarios = Comentario.objects.all()
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)