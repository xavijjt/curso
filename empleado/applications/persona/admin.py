from django.contrib import admin

from .models import Empleado,Habilidades

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        
        
        'id',
        'first_name',
        'lest_name',
        'departamento',
        'job', 
        'full_name',
    )
    
    def full_name(self, obj):
        #toda la operacion
       # print(obj.first_name)
        return obj.first_name + ' ' + obj.lest_name

    search_fields = ('first_name',)
    list_filter =('job',)
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado,EmpleadoAdmin)