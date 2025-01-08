from django.shortcuts import render
from .models import Region

def index(request):
    context = {
        "regiones": Region.objects.all()
    }
    return render(request, 'uno_a_muchos/index.html', context)