from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from . models import Import,Export,Country,Types
# Create your views here.


def home(request):
    return render(request,'home.html',{})

def imports(request):
    
    countrys = Country.objects.all()
    typess = Types.objects.all()
    context = {
        'countrys':countrys,
        'typess':typess
        }
    return render(request,'imports.html',context)


def exports(request):
    c_id=Country.objects.raw("SELECT id FROM CoffeeBrowser_country WHERE CoffeeBrowser_country.name='Indonesia\'")
    t_id=Types.objects.raw("SELECT id FROM CoffeeBrowser_types WHERE CoffeeBrowser_types.Coffee_name='Robusta\'")
    exports = Export.objects.raw(f"SELECT CoffeeBrowser_export.id,CoffeeBrowser_country.name,Coffee_name,E_coffeerate,E_rate_in_INR,E_total_charges,E_IGST,E_shipping_charges FROM CoffeeBrowser_export,CoffeeBrowser_types,CoffeeBrowser_country WHERE CoffeeBrowser_country.id={c_id} AND CoffeeBrowser_types.id={t_id} AND CoffeeBrowser_export.country_id_id={c_id} AND CoffeeBrowser_export.type_id_id={t_id}")
    countrys = Country.objects.all()
    typess = Types.objects.all()
    return render(request,'exports.html',{'exports':exports,'countrys':countrys,'typess':typess})

def about(request):
    return render(request,'about.html',{})

def submitform(request):
    mydictionary= {
        "country": request.GET.get("country"),
        "coffee": request.GET.get("coffee_type"),
        "nbags": request.GET.get("no_of_bags"),
        "method":request.method
    }
    country = mydictionary['country']
    c_id = Country.objects.filter(name = country).values_list('id',flat=True)
    c = c_id[0]
    coffee = mydictionary['coffee']
    t_id = Types.objects.filter(Coffee_name = coffee).values_list('id',flat=True)
    t = t_id[0]
    nbags = int(mydictionary['nbags'])
    imports = Import.objects.raw(f"SELECT CoffeeBrowser_import.id,CoffeeBrowser_country.name,CoffeeBrowser_types.Coffee_name,I_coffeerate,I_rate_in_INR,I_customduty_charges,I_total_charges FROM CoffeeBrowser_import,CoffeeBrowser_types,CoffeeBrowser_country WHERE CoffeeBrowser_country.id={c} AND CoffeeBrowser_types.id={t} AND CoffeeBrowser_import.country_id_id={c} AND CoffeeBrowser_import.type_id_id={t}")
    charges = Import.objects.filter(country_id_id = c, type_id_id = t).values_list('I_total_charges',flat=True)
    charge = charges[0]
    total = nbags*charge
    return render(request,'GetCharges.html',{'imports':imports,'total':total,'nbags':nbags})

