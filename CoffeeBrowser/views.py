from django.shortcuts import render
from django.http import HttpResponse
from . models import Import,Export
# Create your views here.


def home(request):
    imports = Import.objects.all()
    return render(request,'home.html',{'imports':imports})

def imports(request):
    return render(request,'imports.html',{})

def exports(request):
    return render(request,'exports.html',{})

