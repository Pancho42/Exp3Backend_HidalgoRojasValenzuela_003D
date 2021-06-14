from django.urls import path
from . import views

urlpatterns=[
    path('',views.Paginaprincipal, name='Paginaprincipal'),
    path('Productos/',views.Productos, name='Productos'),
    path('QuienesSomos/',views.QuienesSomos, name='QuienesSomos'),
]