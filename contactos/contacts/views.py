from django.shortcuts import render, redirect
from .models import Contacto

def lista_contactos(request):
    contactos = Contacto.objects.all()
    buscar = request.GET.get('buscar', '')
    
    if buscar:
        contactos = contactos.filter(nombre__icontains=buscar) | contactos.filter(correo__icontains=buscar)
    
    # CAMBIA: 'contacts/lista_contactos.html' → 'lista_contactos.html'
    return render(request, 'lista_contactos.html', {
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
            # CAMBIA: 'contacts/agregar_contacto.html' → 'agregar_contacto.html'
            return render(request, 'agregar_contacto.html', {
                'error': 'El correo electrónico no es válido'
            })
        
        Contacto.objects.create(
            nombre=nombre,
            telefono=telefono,
            correo=correo,
            direccion=direccion
        )
        return redirect('lista_contactos')
    
    # CAMBIA: 'contacts/agregar_contacto.html' → 'agregar_contacto.html'
    return render(request, 'agregar_contacto.html')

def editar_contacto(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    
    if request.method == 'POST':
        contacto.nombre = request.POST['nombre']
        contacto.telefono = request.POST['telefono']
        contacto.correo = request.POST['correo']
        contacto.direccion = request.POST['direccion']
        
        if '@' not in contacto.correo or '.' not in contacto.correo:
            # CAMBIA: 'contacts/editar_contacto.html' → 'editar_contacto.html'
            return render(request, 'editar_contacto.html', {
                'contacto': contacto,
                'error': 'El correo electrónico no es válido'
            })
        
        contacto.save()
        return redirect('lista_contactos')
    
    # CAMBIA: 'contacts/editar_contacto.html' → 'editar_contacto.html'
    return render(request, 'editar_contacto.html', {'contacto': contacto})

def eliminar_contacto(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    contacto.delete()
    return redirect('lista_contactos')

def buscar_contactos(request):
    buscar = request.GET.get('buscar', '')
    contactos = Contacto.objects.all()
    
    if buscar:
        contactos = contactos.filter(nombre__icontains=buscar) | contactos.filter(correo__icontains=buscar)
    
    # CAMBIA: 'contacts/buscar_contactos.html' → 'buscar_contactos.html'
    return render(request, 'buscar_contactos.html', {
        'contactos': contactos,
        'buscar': buscar
    })