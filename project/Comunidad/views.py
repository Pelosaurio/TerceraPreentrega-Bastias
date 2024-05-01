from django.shortcuts import render

from . import models

def home(request):
    consulta_comunidad = models.Comunidad.objects.all()
    context = {"comunidades": consulta_comunidad}
    return render(request, "Comunidad/index.html", context)