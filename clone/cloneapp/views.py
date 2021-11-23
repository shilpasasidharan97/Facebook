from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('WELCOME')

def ind(request):
    return render(request,'index.html')


def data(request):
    return render(request,'data.html')

def table(request):
    return render(request,'table.html')

def login(request):
    return render(request,'fb.html')