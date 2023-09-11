from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appName' : 'Curry Under Armour Inventory',
        'name' : 'Muhammad Sean Arsha Galant',
        'class': 'International Class'
    }

    return render(request, 'main.html', context)