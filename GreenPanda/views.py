from django.shortcuts import render

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

    return render(request, 'Comentarios.html'

      

    )

def CrearComentario(request):

    return render(request, 'CrearComentario.html'

      

    )