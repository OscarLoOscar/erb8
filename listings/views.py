from django.shortcuts import render,get_object_or_404
from listings.models import Listing
from django.core.paginator import Paginator
# Create your views here.
# 3.最終分黎呢度，2個endpoint
def listings(request):
  # print(request.path) # /listings/
  listings = Listing.objects.filter(is_published=True)
  paginator = Paginator(listings,3)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)
  content = {'listings':paged_listings}
  return render(request,'listings/listings.html',content)
# ('pages/index.html')

def listing(request,listing_id):
  # return HttpResponse('<h1>about</h1>')
  listing = get_object_or_404(Listing,pk=listing_id)
  content = {'listing':listing}
  return render(request,'listings/listing.html',content)

def search(request):
  return render(request,'listings/search.html')