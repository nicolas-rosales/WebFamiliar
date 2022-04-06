from django import forms

class FamiliarForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_nacimiento = forms.DateField()
    parentesco = forms.CharField()





