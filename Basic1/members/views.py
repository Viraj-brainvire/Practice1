from django.shortcuts import render
from django.http import HttpResponse
from django.template import  loader 
from django.shortcuts import render
# Create your views here.
def first(request):
    return HttpResponse('Hello World ! ')

def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())