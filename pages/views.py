from django.shortcuts import render
# from django.http import HttpResponse
from listings.models import Listing
from doctors.models import Doctor

# Create your views here.
# 3.最終分黎呢度，2個endpoint
# def index(request):
#   return render(request,'pages/index.html')
# ('pages/index.html')
# pass 個dictionary入黎:
def index(request):
  # listings = Listing.objects.all() # 大階Listing，拎data model，all() -> 同DB溝通，拎晒所有data
  listings = Listing.objects.order_by('list_date').filter(is_published=True)[:3] # [:3] -> list -> 0,1,2
  context = {"listings" : listings}
  # return render(request,'pages/index.html',{'anything' : 'something','numbers': 1234})
  return render(request,'pages/index.html',context) # 之後會多database，但煩，難改，方便加model

def about(request):
  # return HttpResponse('<h1>about</h1>')
  doctors = Doctor.objects.order_by('-hire_date')[:3]
  mvp_doctors = Doctor.objects.all().filter(is_mvp=True)
  total_mvp = mvp_doctors.count()
  context = {"doctors":doctors,"mvp_doctors":mvp_doctors}
  return render(request,'pages/about.html',context)

# def listing(request):
#   return render(request,'pages/listings.html')

# Django Function Base writing
# DONT use Class Base