from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Ahoj světe!")
# Create your views here.
