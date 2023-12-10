from django.shortcuts import render

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
    return render(request, "core/cotizador.html")

def blog(request):
    return render(request, "core/blog.html")

def contacto(request):
    return render(request, "core/contacto.html")

