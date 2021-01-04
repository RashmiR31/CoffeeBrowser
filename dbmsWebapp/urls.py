"""dbmsWebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from CoffeeBrowser import views
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',views.home,name='home'),
    path('imports/',views.imports,name='imports'),
    path('exports/',views.exports,name='exports'),
    path('about/',views.about,name='about'),
    path('submitform/',views.submitform,name="submitform"),
    path('exportsdata/',views.exportsdata,name="exportsdata"),
    path('accounts/', include('allauth.urls')),
    path('survey/',views.survey,name='survey'),
    path('survey_results/',views.survey_results,name="survey_results"),
]

