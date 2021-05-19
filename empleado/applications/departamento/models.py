from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField("nombre", max_length=50)
    shor_name=models.CharField("nombreCorto", max_length=50)
    anulate= models.BooleanField("anulado",default=False)

    class Meta:
        verbose_name='Mi Departamento'
        verbose_name_plural='Areas de la Empresa'
        ordering=['-name']
        unique_together=('name','shor_name')
    
    def __str__(self):
        return str(self.id)+'-'+self.name+'-'+self.shor_name

