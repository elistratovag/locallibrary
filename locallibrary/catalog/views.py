from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    #data = request.META
    data = ''
    for key, value in request.META.items():
        data += '{}-{}<br />'.format(key, value) 
    return HttpResponse(data) 