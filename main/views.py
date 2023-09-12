# Create your views here.
from django.shortcuts import render
def show_main(request):
    context = {
        'nama_aplikasi': 'Pacil Mart',
        'name' : 'Rafah Azizah' ,
        'kelas': 'PBP D',

    }

    return render(request, "main.html", context)