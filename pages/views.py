from django.shortcuts import render
# from django.http import HttpResponse
from listings.models import Listing
# Create your views here.
# 3.最終分黎呢度，2個endpoint
# def index(request):
#   return render(request,'pages/index.html')
# ('pages/index.html')
# pass 個dictionary入黎:
def index(request):
  listings = Listing.objects.all() # 大階Listing，拎data model，all() -> 同DB溝通，拎晒所有data
  content = {"listings" : listings}
  # return render(request,'pages/index.html',{'anything' : 'something','numbers': 1234})
  return render(request,'pages/index.html',content) # 之後會多database，但煩，難改，方便加model

def about(request):
  # return HttpResponse('<h1>about</h1>')
  return render(request,'pages/about.html')

def listing(request):
  return render(request,'pages/listings.html')