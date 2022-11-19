from django.shortcuts import render

from django.http import HttpResponse



def index(request):
    return render(request, "english/index.html")
def trending(request):
    return render(request, "english/trending.html")
def channel(request):
    return render(request, "english/channel.html")

# def index(request):
#     return HttpResponse("Welcome English Web")