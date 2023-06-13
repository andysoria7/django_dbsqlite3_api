from django.db import models

# Create your models here.

class Company(models.Model):
    name= models.CharField(max_length=50)
    website= models.URLField(max_length=100)
    foundation= models.PositiveIntegerField()
    
    def __str__(self): # Metodo especial para permitir decirle lo que muestro en el admin de django.
        return self.name  # Muestra en la tabla de django por name concatenado por nombre de proyecto.
