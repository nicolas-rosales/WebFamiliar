from django.db import models


class Familiar(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} - {self.fecha_nacimiento} - {self.parentesco}"
    
     
