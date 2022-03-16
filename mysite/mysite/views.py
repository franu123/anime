from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def home(request):
    res = render(request, 'home.html')
    return HttpResponse(res)
