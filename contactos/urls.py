# En el archivo urls.py principal de tu proyecto

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ÚNICA ruta raíz: incluye la aplicación 'contactos'
    path('', include('agenda.urls')),
]