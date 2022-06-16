from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from contacto.models import Mensaje
from .forms import MensajeForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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
 
    return redirect('listar_mensaje')
 
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
    
# def index(request):
#     return render(
#         request,
#         "index.html",
#         {
#             'title' : "index HelloDjangoApp",
#             'content' : "Example app page for Django."
#         }
#     )
    
def index(request):
    return render(request,'index.html')


