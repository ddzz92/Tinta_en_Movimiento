from django.urls import path
from . import views

urlpatterns = [    
    path('blog', views.blog, name="blog"),
    path('articuloblog1/', views.articuloblog1, name="articuloblog1"),
    path('articuloblog2/', views.articuloblog2, name="articuloblog2"),
    path('articuloblog3/', views.articuloblog3, name="articuloblog3"),
]