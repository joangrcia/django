from django.shortcuts import render

def index(request):
    context = {
        'judul':'Juan Garcia',
        'subjudul':'Home',
    }
    return render(request, 'index.html', context)