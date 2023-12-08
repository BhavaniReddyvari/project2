from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohith(request):
    return render(request,'rohith.html')

def maxwell(request):
    return HttpResponse("Important batsman ")