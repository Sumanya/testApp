from http.client import HTTPResponse
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Index here")