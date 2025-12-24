from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 3.最終分黎呢度，2個endpoint
def index(request):
  return render(request,'pages/index.html')
# ('pages/index.html')

def about(request):
  # return HttpResponse('<h1>about</h1>')
  return render(request,'pages/about.html')

def listing(request):
  return render(request,'pages/listing.html')