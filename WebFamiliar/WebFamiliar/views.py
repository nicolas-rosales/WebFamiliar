from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from FamiliaApp.models import Familiar

def InicioPage(request):
    Familiar.nombre = Familiar.objects.all()

    contexto = {"producto":Familiar.nombre}
    return render(request, "InicioPage.html", contexto)
