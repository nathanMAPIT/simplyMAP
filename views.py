from django.shortcuts import render

def index(request):
    return render(request, 'smplmapDEV1/home.html')
