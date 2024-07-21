from django.db import models

# Create your models here.
class  Artista(models.Model):
    nombre =models.CharField('nombre del artista:',max_length=100,blank=False,null=False)
    telefono=models.CharField('telefono del artista:',max_length=100,blank=False,null=False)
    class Meta:
        db_table="Artista" 
    def __str__(self):
        return self.nombre + ' ' + self.telefono    
class Cancion(models.Model):
    nombreCa = models.CharField('Cancion:', max_length = 100, null = False, blank = False)
    Fecha_Publicacion = models.DateField()
    Artista = models.ForeignKey(Artista, on_delete = models.DO_NOTHING,related_name='Canciones')

    def __str__(self):
        return self.nombreCa

    class Meta:
        db_table = 'Cancion'    