from django.shortcuts import render
from django.http import HttpResponse
from . models import Import,Export
# Create your views here.


def home(request):
    return render(request,'home.html',{})

def imports(request):
    imports = Import.objects.all()
    return render(request,'imports.html',{'imports':imports})

def exports(request):
    exports = Export.objects.all()
    return render(request,'exports.html',{'exports':exports})

def about(request):
    return render(request,'about.html',{})


