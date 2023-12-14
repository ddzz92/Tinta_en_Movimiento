from django.db import models

# Create your models here.
opciones_largo_tatuaje =[
    [0, "10 centímetros"],
    [1, "15 centímetros"],
    [2, "20 centímetros"],
    [3, "25 centímetros"],
    [4, "30 centímetros"]
]

opciones_ancho_tatuaje =[
    [0, "10 centímetros"],
    [1, "15 centímetros"],
    [2, "20 centímetros"],
    [3, "25 centímetros"],
    [4, "30 centímetros"]
]

opciones_partes =[
    [0, "brazo"],
    [1, "pierna"],
    [2, "pecho"],
    [3, "espalda"],
    [4, "abdomen"],
    [5, "mano"],
    [6, "otro"]
]

opciones_color =[
    [0, "color"],
    [1, "negro"],
    [2, "indeciso"],
]



opciones_consutas =[
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consutas)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre
    
    
class Turnos(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    largo_del_tatuaje = models.IntegerField(choices=opciones_largo_tatuaje)
    ancho_del_tatuaje = models.IntegerField(choices=opciones_ancho_tatuaje)
    parte_del_cuerpo_del_tatuaje = models.IntegerField(choices=opciones_partes)
    a_color_o_en_negro = models.IntegerField(choices=opciones_color)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre