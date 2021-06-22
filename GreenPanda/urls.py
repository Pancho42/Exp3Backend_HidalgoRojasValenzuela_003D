from django.urls import path
from . import views

urlpatterns=[
    path('',views.Paginaprincipal, name='Paginaprincipal'),
    path('Productos/',views.Productos, name='Productos'),
    path('QuienesSomos/',views.QuienesSomos, name='QuienesSomos'),
    path('Registro/',views.Registro, name='Registro'),
    path('Despacho/',views.Despacho, name='Despacho'),
    path('Comentarios/',views.Comentarios, name='Comentarios'),
    path('CrearComentario/',views.CrearComentario, name='CrearComentario'),
    path('ModComentario/<id>',views.ModComentario, name='ModComentario'),
]