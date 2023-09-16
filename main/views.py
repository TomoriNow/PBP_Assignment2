from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ProductForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    products = Item.objects.all()
    
    context = {
        'appName' : 'Curry Under Armour Inventory',
        'name' : 'Muhammad Sean Arsha Galant',
        'class': 'PBP International Class',
        'description' : "The game’s most dynamic player needs basketball shoes that can keep up with him. Steph Curry basketball shoes are built from super-lightweight, breathable materials, and use our top cushioning like UA Flow and UA HOVR™ to cushion your landings and propel you forward.",
        'release_date' : '11 September 2023',
        'products' : products
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
    
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")