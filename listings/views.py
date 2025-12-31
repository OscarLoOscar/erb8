from django.shortcuts import render,get_object_or_404
from listings.models import Listing
from django.core.paginator import Paginator
from listings.choices import district_choices,bedroom_choices,room_type_choices
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
  # get all data
  queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)

  # filter keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(title__icontains=keywords)
  
  # filter district
  if 'district' in request.GET:
    district = request.GET['district']
    if district:
      queryset_list = queryset_list.filter(district__iexact=district)

  # filter room
  if 'rooms' in request.GET:
    rooms = request.GET['rooms']
    if rooms:
      queryset_list = queryset_list.filter(rooms=rooms)

  # filter roomtype
  if 'room_type' in request.GET:
    room_type = request.GET['room_type']
    if room_type:
      queryset_list = queryset_list.filter(room_type__iexact=room_type)

  context = {
        'district_choices': district_choices,
        'bedroom_choices': bedroom_choices,
        'room_type_choices': room_type_choices,
        'listings':queryset_list,
        'values':request.GET
    }
  return render(request,'listings/search.html',context)