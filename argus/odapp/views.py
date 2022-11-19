from django.shortcuts import render

from django.http import HttpResponse




def index(request):
    return render(request, "odia/index.html")
def trending(request):
    return render(request, "odia/trending.html")
def channel(request):
    return render(request, "odia/channel.html")

# def index(request):
#     return HttpResponse("Welcome Odia web")