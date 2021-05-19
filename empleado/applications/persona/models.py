from django.db import models

from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades (models.Model):
    habilidad = models.CharField('Habilidad',max_length=50)
    
    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades empleados'
        
      
    
    def __str__(self):
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):
    JOB_CHOICES=(
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Ecosistema'),
        ('3','Sistema')
    )
    
    
    first_name = models.CharField('Nombre', max_length=50)
    lest_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField('Nombres completos', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1,choices=JOB_CHOICES)
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado',blank=True,null = True )
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name='Persona'
        verbose_name_plural='Trabajador'
        ordering=['-first_name']
      
    
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.lest_name
