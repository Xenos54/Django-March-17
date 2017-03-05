from django.shortcuts import render

def index(request):
    name = 'gold'
    value = 100.00
    context = {'treasure_name': name, 'treasure_value': value }

    return render(request, 'index.html', context)


# Create your views here.
