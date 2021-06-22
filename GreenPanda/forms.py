from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Resenna, ComentarioC


class ComentarioForm(forms.ModelForm):

    class Meta:
        model= ComentarioC
        fields = ['NombreC', 'comentario', 'resenna']
        labels ={
            'NombreC': 'Nombre Completo',
            'comentario': 'Comentario',
            'resenna': 'Resenna',
        }
        widgets={
            'NombreC': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ),
            'comentario': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Max 150 caracteres', 
                    'id': 'comentario',
                    'rows':8,
                    'cols':80  
                }
            ),
            'resenna': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tiporesenna',
                }
            )
        }