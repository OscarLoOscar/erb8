from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.
# step 2 , define function
def login(request):
  if request.method == 'POST':
    username = request.POST.get('username') # ['username']
    # password = request.POST['password']
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      messages.success(request,'You are now logged in.')
      return redirect('accounts:dashboard')
    else:
      messages.error(request,'Invalid credentials')
      return redirect('accounts:login') # redirect to endpoint, don't add .html, render requires .html
  else:
    return render(request,'accounts/login.html')

def logout(request):
  if request.method=="POST":
    auth.logout(request)
    messages.success(request,'You are now logged out.')
    return redirect('pages:index')
  return redirect('pages:index')   

def register(request):
  if request.method == 'POST':
    # handle registration logic here
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request,"Username already exists.")
        return redirect("accounts:register")
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request,"Email already exists.")
          return redirect("accounts:register")
        else:
          user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
          user.save()
          messages.success(request,'You are now registered and can login.')
          return redirect("accounts:login")
    else:
      messages.error(request,'Passwords do not match')
      return redirect("accounts:register")
  else:
    return render(request,'accounts/register.html')

def dashboard(request):
  # 一定login左，exist user， Contact searching database
  # 點解係accounts/views.py, not contacts/views.py?
  # Welcome {{user.first_name}} 係come from accounts/views.py
  user_contacts = Contact.objects.all().filter(user_id=request.user.id).order_by('-contact_date')
  # all()加唔加都得
  context = {"contacts": user_contacts}
  return render(request,'accounts/dashboard.html',context)

# 一次分流分app
# 二次分流分endpoint
# 要做晒諗晒有幾多個endpoint先做