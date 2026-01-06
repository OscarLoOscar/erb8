from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact
from django.contrib import messages
from .forms import ContactForm
# Create your views here.
def contacts(request):
  if request=="POST":
    listing = request.POST['listing']
    listing_id = request.POST['listing_id']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    if request.user.is_authenticated:
      has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
      if has_contacted:
        messages.error(request,'You have already made an inquiry for this listing')
        return redirect('listing:listing', listing_id=listing_id)
      contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
      contact.save()
      messages.success(request,'Your request has been submitted, a realtor will get back to you soon')
      return redirect('listings:listing', listing_id=listing_id)
  return render(request,'listings/listings.html')

def delete_contact(request,contact_id):
  # contact = Contact.objects.get(id=contact_id)
  # contact.delete()
  # messages.success(request,'Contact deleted successfully.')
  contact = get_object_or_404(Contact,id=contact_id)
  contact.delete()
  # 唔放message原因： 因為已經係modal confirm左delete, 再放message會重覆
  return redirect('accounts:dashboard')

def edit_contact(request,contact_id):
  contact = get_object_or_404(Contact,id=contact_id)
  if request.method =="POST":
    form = ContactForm(request.POST,instance=contact)
    if form.is_valid():
      form.save()
    return redirect('accounts:dashboard')
  else:
    form=ContactForm(instance=contact)
    
  return render(request,'contacts/edit_contact.html',{"form":form , "contact":contact})

# in Django
# render(request, 'template.html', context)：必須要放 request。
# redirect('url_name')：絕對唔可以放 request 喺第一個位。