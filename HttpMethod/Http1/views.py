from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse,HttpResponseNotFound ,JsonResponse
from .models import data
from .forms import DataForm
import datetime
# Create your views here.
def simple(request):
    context = {'data' : data.objects.all()}
    return render(request, "Data/data.html", context)

@require_http_methods(['GET','POST'])
def method1(request):
    if request.method == 'GET':
        return HttpResponse("Data has been fetched")
    elif request.method == 'POST':
        return HttpResponse("Data has been added ")
    
def method2(request,id=0):
    if request.method == "GET":
        if id==0:
            form = DataForm()
        else:
            employee = data.objects.get(pk = id)
            form = DataForm(instance = employee)
        return render(request, "Data/form.html",{'form':form})
    else:
        if id==0:
            form = DataForm(request.POST)
        else:
            employee = data.objects.get(pk = id)
            form = DataForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/Home')


def method3(request,id):
        employee = data.objects.get(pk = id)
        employee.delete()
        return redirect('/Home')

def my_view(request):
    if id == 0:
        return HttpResponseNotFound("<h1>Page not found </h1>")
    else:
        return HttpResponse("<h1>Page found</h1>")
    
def my_view1(request):
    return HttpResponseNotFound("<h1>Page not found </h1>")

def response_error_handler(request, exception=None):
    return HttpResponse("Error handler content", status=403)

async def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)