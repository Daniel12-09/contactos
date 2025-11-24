from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
   
    list_display = ('nombre', 'telefono', 'correo', 'direccion')

    
    search_fields = ('nombre', 'correo', 'telefono')

 
    list_filter = ('correo',)

 
    ordering = ('nombre',)

   
    readonly_fields = ()

 
    fieldsets = (
        ('Información de contacto', {
            'fields': ('nombre', 'telefono', 'correo', 'direccion')
        }),
    )

  
    list_per_page = 10
