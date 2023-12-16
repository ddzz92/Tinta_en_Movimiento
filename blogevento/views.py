from django.shortcuts import render
from .models import blog_evento

# Create your views here.
def articuloblog3(request):
    blog_eventos = blog_evento.objects.all()
    return render(request, "blogevento/articuloblog3.html", {'blog_eventos':blog_eventos})