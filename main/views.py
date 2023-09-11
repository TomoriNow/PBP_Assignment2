from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appName' : 'Curry Under Armour Inventory',
        'name' : 'Muhammad Sean Arsha Galant',
        'class': 'PBP International Class',
        'description' : "The game’s most dynamic player needs basketball shoes that can keep up with him. Steph Curry basketball shoes are built from super-lightweight, breathable materials, and use our top cushioning like UA Flow and UA HOVR™ to cushion your landings and propel you forward.",
        'release date' : '11 September 2023',
        'amount' : '30'
    }

    return render(request, 'main.html', context)