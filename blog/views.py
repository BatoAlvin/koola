from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm


# Create your views here.
def home(request):
   context = {'home': Employee.objects.all()}
   return render(request ,'home.html', context)       

def login(request):
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
         auth.login(request, user)
         return redirect('/home')
      else:
          messages.error(request, 'Invalid details') 
          return redirect('/login')  
    else:
        return render(request, 'login.html')  

def register(request):
   if request.method == 'POST':
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      username = request.POST['username']
      password1 = request.POST['password1']
      password2 = request.POST['password2']
      email = request.POST['email']

      if password1 == password2:
         if User.objects.filter(username=username).exists():
            messages.error(request, 'Username taken')
            return redirect('/')
         elif User.objects.filter(email=email).exists():
              messages.error(request, 'Email taken')
              return redirect('/')
         else:        
              user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
              user.save();
              print('user created')
              return redirect('/login')
      else:
           messages.error(request, 'Password mismatch')
           return redirect('/')        
      return redirect('/home')
   else:
         return render(request ,'register.html')

def logout(request):
      auth.logout(request)
      return redirect('/home')         
     
def records(request,id=0):
   if request.method == 'GET':
      if id==0:
         form = EmployeeForm()
      else:
         customer = Employee.objects.get(pk=id)
         form = EmployeeForm(instance=customer)   
      return render(request, 'records.html', {'form':form})
   else:
      if id == 0:
         form = EmployeeForm(request.POST)
      else:
         customer = Employee.objects.get(pk=id)   
         form = EmployeeForm(request.POST, instance=customer)
      
      if form.is_valid():
         form.save();   
      return redirect('/home')   

def records_delete(request,id):
   customer = Employee.objects.get(pk=id)
   customer.delete()
   return redirect('/home')
  
