from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Contacto
from .serializers import GroupSerializer, UserSerializer, ContactoSerializer 




class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all().order_by("nombre")
    serializer_class = ContactoSerializer
    permission_classes = [permissions.IsAuthenticated] 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



def lista_contactos(request):
    contactos = Contacto.objects.all()
    buscar = request.GET.get('buscar', '')
    
    if buscar:
        contactos = contactos.filter(nombre__icontains=buscar) | contactos.filter(correo__icontains=buscar)
    
    return render(request, 'contacts/lista_contactos.html', {
        'contactos': contactos,
        'buscar': buscar
    })

def agregar_contacto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        direccion = request.POST['direccion']
        
        if '@' not in correo or '.' not in correo:
            return render(request, 'contacts/agregar_contacto.html', {
                'error': 'El correo electrónico no es válido'
            })
        
        Contacto.objects.create(
            nombre=nombre,
            telefono=telefono,
            correo=correo,
            direccion=direccion
        )
        return redirect('lista_contactos')
    
    return render(request, 'contacts/agregar_contacto.html')

def editar_contacto(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    
    if request.method == 'POST':
        contacto.nombre = request.POST['nombre']
        contacto.telefono = request.POST['telefono']
        contacto.correo = request.POST['correo']
        contacto.direccion = request.POST['direccion']
        
        if '@' not in contacto.correo or '.' not in contacto.correo:
            return render(request, 'contacts/editar_contacto.html', {
                'contacto': contacto,
                'error': 'El correo electrónico no es válido'
            })
        
        contacto.save()
        return redirect('lista_contactos')
    
    return render(request, 'contacts/editar_contacto.html', {'contacto': contacto})

def eliminar_contacto(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    contacto.delete()
    return redirect('lista_contactos')

def buscar_contactos(request):
    buscar = request.GET.get('buscar', '')
    contactos = Contacto.objects.all()
    
    if buscar:
        contactos = contactos.filter(nombre__icontains=buscar) | contactos.filter(correo__icontains=buscar)
    
    return render(request, 'contacts/buscar_contactos.html', {
        'contactos': contactos,
        'buscar': buscar
    })