from django.shortcuts import render
from django.http import HttpResponse
from . import views


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Beka', 'age': 24, 'department': 'cs'})


def add(request):
    val1 = int(request.GET.get("num1", 0))
    val2 = int(request.GET.get("num2", 0))
    res = val1 + val2
    return render(request, "result.html", {'result': res})