
from django.urls import path
from django.views import *

from .views import FamiliaForm, FamiliaRead, InicioPage

urlpatterns = [
    path('webfamiliar/', InicioPage, name="webfamiliar"),
    path('cargarfamiliar/', FamiliaForm, name="cargarfamiliar"),
    path('familiaread/', FamiliaRead, name="familiaread"),
]