from django.shortcuts import render

from . import models

def home(request):
    query = models.Comunidad.objects.all()
    context = {"comunidades": query}
    return render(request, "Comunidad/index.html", context)