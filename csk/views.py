from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return render(request,'msd.html')

def abd(request):
    return HttpResponse('<h1>Important person in csk</h1>')
