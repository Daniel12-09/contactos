# En agenda/urls.py

from django.urls import path, include
from rest_framework import routers
from . import views 

# 🚨 IMPORTACIONES DE JWT 🚨
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Configuración del Router para la API REST
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"contactos", views.ContactoViewSet) 

# Definición de patrones de URL 
urlpatterns = [
    # Rutas de Autenticación JWT (Paso 3)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Rutas de la API (DRF)
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    
    # Rutas de Vistas Regulares (HTML/Templates)
    path('', views.lista_contactos, name='lista_contactos'),
    path('agregar/', views.agregar_contacto, name='agregar_contacto'),
    path('editar/<int:contacto_id>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:contacto_id>/', views.eliminar_contacto, name='eliminar_contacto'),
    path('buscar/', views.buscar_contactos, name='buscar_contactos'),
]