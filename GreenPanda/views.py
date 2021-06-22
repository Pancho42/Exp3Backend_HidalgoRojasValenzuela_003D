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