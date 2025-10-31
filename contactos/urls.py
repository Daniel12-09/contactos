from django.contrib import admin
from django.urls import path
from contacts import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_contactos, name='lista_contactos'),
    path('agregar/', views.agregar_contacto, name='agregar_contacto'),
    path('editar/<int:contacto_id>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:contacto_id>/', views.eliminar_contacto, name='eliminar_contacto'),
    path('buscar/', views.buscar_contactos, name='buscar_contactos'),
]