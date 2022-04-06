from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from FamiliaApp.forms import FamiliarForm
from .models import Familiar

def InicioPage(request):
    return render(request, "InicioPage.html")

def FamiliaRead(request):
    familia = Familiar.objects.all()

    contexto = {"familia":familia}
    return render(request, "FamiliaRead.html", contexto)

def FamiliaForm(request):
    if request.method == 'POST':
        formulario = FamiliarForm(request.POST)
        print(formulario)
        
        if formulario.is_valid:
            dataform = formulario.cleaned_data
            familiar = Familiar(nombre=dataform['nombre'],
                                apellido=dataform['apellido'],
                                fecha_nacimiento=dataform['fecha_nacimiento'],
                                parentesco=dataform['parentesco'] )
            familiar.save()
            return render(request, 'InicioPage.html')
    else:
        formulario = FamiliarForm()
    return render(request, 'FamiliaForm.html',{"formulario":formulario})
    