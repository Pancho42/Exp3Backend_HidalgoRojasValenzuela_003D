from django.shortcuts import render, redirect
from .models import ComentarioC
from .forms import ComentarioForm

# Create your views here.

def Paginaprincipal(request):

    return render(request, 'Paginaprincipal.html'

      

    )

def Productos(request):

    return render(request, 'Productos.html'

      

    )

def QuienesSomos(request):

    return render(request, 'QuienesSomos.html'

      

    )

def Registro(request):

    return render(request, 'Registro.html'

      

    )

def Despacho(request):

    return render(request, 'Despacho.html'

      

    )

def Comentarios(request):

    comentarios = ComentarioC.objects.all

    
    
    return render(request, 'Comentarios.html', context ={ 'datos':comentarios},
    
    
    
    )

def CrearComentario(request):
    if request.method=='POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario_form.save()
            return redirect('Comentarios')
    else:
        comentario_form= ComentarioForm()
    return render(request, 'GreenPanda/CrearComentario.html', {'comentario_form': comentario_form}

      

    )

def ModComentario(request,id):
    comentario = ComentarioC.objects.get(NombreC=id)

    com ={
        'form': ComentarioForm(instance=comentario)
    }
    if request.method=='POST':
        formulario = ComentarioForm(data=request.POST, instance = comentario)
        if formulario.is_valid:
            formulario.save()
            return redirect('Comentarios')
    
    
    return render(request, 'GreenPanda/ModComentario.html', com
    
    
    
    )

def eliminar(request,id):
    comentario = ComentarioC.objects.get(NombreC=id)
    comentario.delete()
    return redirect('Comentarios')

