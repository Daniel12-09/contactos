from django.shortcuts import render, redirect
from .models import Contacto

def lista_contactos(request):
    """Vista para mostrar todos los contactos"""
    # Obtener todos los contactos de la base de datos
    contactos = Contacto.objects.all()
    
    # Obtener término de búsqueda si existe
    buscar = request.GET.get('buscar', '')
    
    # Filtrar contactos si hay búsqueda
    if buscar:
        contactos = contactos.filter(nombre__icontains=buscar) | contactos.filter(correo__icontains=buscar)
    
    # Pasar los contactos al template
    return render(request, 'lista_contactos.html', {
        'contactos': contactos,
        'buscar': buscar
    })

def agregar_contacto(request):
    """Vista para agregar un nuevo contacto"""
    if request.method == 'POST':
        # Si el formulario fue enviado (POST)
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        direccion = request.POST['direccion']
        
        # Validación simple del correo
        if '@' not in correo or '.' not in correo:
            # Si el correo no es válido, mostrar error
            return render(request, 'agregar_contacto.html', {
                'error': 'El correo electrónico no es válido'
            })
        
        # Crear y guardar el nuevo contacto
        Contacto.objects.create(
            nombre=nombre,
            telefono=telefono,
            correo=correo,
            direccion=direccion
        )
        
        # Redirigir a la lista de contactos
        return redirect('lista_contactos')
    
    # Si es GET, mostrar el formulario vacío
    return render(request, 'agregar_contacto.html')

def editar_contacto(request, contacto_id):
    """Vista para editar un contacto existente"""
    # Obtener el contacto por su ID
    contacto = Contacto.objects.get(id=contacto_id)
    
    if request.method == 'POST':
        # Actualizar los datos del contacto
        contacto.nombre = request.POST['nombre']
        contacto.telefono = request.POST['telefono']
        contacto.correo = request.POST['correo']
        contacto.direccion = request.POST['direccion']
        
        # Validar correo
        if '@' not in contacto.correo or '.' not in contacto.correo:
            return render(request, 'editar_contacto.html', {
                'contacto': contacto,
                'error': 'El correo electrónico no es válido'
            })
        
        # Guardar los cambios
        contacto.save()
        return redirect('lista_contactos')
    
    # Mostrar formulario con datos actuales
    return render(request, 'editar_contacto.html', {'contacto': contacto})

def eliminar_contacto(request, contacto_id):
    """Vista para eliminar un contacto"""
    contacto = Contacto.objects.get(id=contacto_id)
    contacto.delete()  # Eliminar el contacto
    return redirect('lista_contactos')

def buscar_contactos(request):
    """Vista específica para búsqueda de contactos"""
    buscar = request.GET.get('buscar', '')
    contactos = Contacto.objects.all()
    
    # Filtrar si hay búsqueda
    if buscar:
        contactos = contactos.filter(nombre__icontains=buscar) | contactos.filter(correo__icontains=buscar)
    
    return render(request, 'buscar_contactos.html', {
        'contactos': contactos,
        'buscar': buscar
    })