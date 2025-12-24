from django.shortcuts import render
# Create your views here.
# 3.最終分黎呢度，2個endpoint
def listings(request):
  # print(request.path) # /listings/
  return render(request,'listings/listings.html')
# ('pages/index.html')

def listing(request,listing_id):
  # return HttpResponse('<h1>about</h1>')
  return render(request,'listings/listing.html')

def search(request):
  return render(request,'listings/search.html')