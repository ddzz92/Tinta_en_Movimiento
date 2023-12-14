from django.shortcuts import render

def blog(request):
    return render(request, "blog_/templates/blog.html")

def articuloblog1(request):
    return render(request, "blog_/templates/articuloblog1.html")

def articuloblog2(request):
    return render(request, "blog_/templates/articuloblog2.html")

def articuloblog3(request):
    return render(request, "blog_/templates/articuloblog3.html")
