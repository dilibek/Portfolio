from django.shortcuts import render
from .models import *

# Create your views here.
def HomeView(request):
    context = {
        'info': Info.objects.first(),
        'bio': Bio.objects.first(),
        'smedia': SMedia.objects.all(),
        'skills': Skills.objects.all(),
    }

    return render(request, 'index.html', context)
