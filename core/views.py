from django.shortcuts import render
from .forms import ContactoForm, TurnosForm


# Create your views here.
def home(request):
    return render(request, "core/home.html")

def estudio(request):
    return render(request,  "core/estudio.html")

def equipo(request):
    return render(request, "core/equipo.html")

def portafolio(request):
    return render(request, "core/portafolio.html")

def cuidados(request):
    return render(request, "core/cuidados.html")

def cotizador(request):
    data={
        'form': TurnosForm()
    }
    if request.method == 'POST':
        formulariot = TurnosForm(data=request.POST)
        if formulariot.is_valid():
            formulariot.save()
            data["mensaje"]= "Solicitud enviada"
        else:
            data['form']= formulariot
    return render(request, "core/cotizador.html", data)

def blog(request):
    return render(request, "core/blog.html")

def contacto(request):
    data={
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Mensaje enviado"
        else:
            data['form']= formulario
    return render(request, 'core/contacto.html',data)

def articuloblog1(request):
    return render(request, "core/articuloblog1.html")

def articuloblog2(request):
    return render(request, "core/articuloblog2.html")