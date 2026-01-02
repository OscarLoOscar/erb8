from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
# step 2 , define function
def login(request):
  return render(request,'accounts/login.html')

def logout(request):
  return render(request,'accounts/logout.html')

def register(request):
  if register.method == 'POST':
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
          pass
    else:
      messages.error(request,'Passwords do not match')
      return redirect("accounts:register")
    pass
  else:
    return render(request,'accounts/register.html')

def dashboard(request):
  return render(request,'accounts/dashboard.html')