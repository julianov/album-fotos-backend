from django.db import models

# Create your models here.



class Fotos(models.Model):
    #user = models.CharField(max_length=200)
    
    numero = models.IntegerField(default=0)
    foto=models.ImageField(upload_to='media/', blank=True)	
    descripcion= models.TextField(blank = True)
    categoria = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.foto

    def filas (self):
        return ( len( Fotos.objects.all() ) )