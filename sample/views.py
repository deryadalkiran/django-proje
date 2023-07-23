from django.shortcuts import render
from sample.models import Sample

# Create your views here.

def index(request):
    
    context = dict()

    context['samples'] = Sample.objects.all()  #select* from sample

    return render(request, 'index.html', context)
