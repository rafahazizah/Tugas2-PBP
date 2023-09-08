# Create your views here.
from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Lifebuoy',
        'Amount': '10',
        'Description' : 'Sabun',
        
    }

    return render(request, "main.html", context)