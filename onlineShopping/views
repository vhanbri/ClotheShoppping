from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from onlineShopping.models import User
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
# Create your views here.
class LogOutView (View):
    def get(self, request):
        logout(request)
        messages.success(self.request, "Logged out!")
        return redirect('/login')
class logInView(View):
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page.
                userSession = request.user or "none"
                messages.success(self.request, 'Signed in succesfully')
                return HttpResponseRedirect("/", {'user': userSession})
        
            else:
                # Return an 'invalid login' error message.
                messages.error(self.request, 'Wrong username or password!')
                return redirect('/login')
        

    def get(self, request):
        storage = messages.get_messages(request)
        for _ in storage:
            # This is important
            # Without this loop `_loaded_messages` is empty
            pass
        return render(request, 'login.html', {})
        

class MyIndexView(View):
         def get(self, request):
        
          return render(request, 'index.html', {})
       
class AboutView(View):
       def get(self, request):
        
          return render(request, 'about.html', {})

class ContactView(View):
        def get(self, request):
        
          return render(request, 'contact.html', {})
class RegisterView(View):
 def post(self, request):
          if request.method == 'POST':
                User.objects.all().count()+1
                user = User()
                user.firstname = request.POST.get('Firstname')
                user.lastname = request.POST.get('Lastname')
                user.phoneNumber = request.POST.get('contact')
                user.username = request.POST.get('username')
                user.password = request.POST.get('password')
                
               
              
          if(User.objects.filter(username = user.username).exists()):
                        messages.error(self.request, 'USER EXIST!')
                        return redirect('/register')
          else:  
                        user.save()
                        messages.success(self.request, 'SUCCESS')
                        return redirect('/register')
 def get(self, request):
        storage = messages.get_messages(request)
        for _ in storage:
            # This is important
            # Without this loop `_loaded_messages` is empty
            pass
        return render(request, 'register.html', {})



class DashboardView(View):
 
  ##def post(self, request):   
       ##    if request.method == 'POST':
          ##      request.POST.get('insert') == 'tbl_us
          ##      use = User()
          ##      use.patient_id = request.POST.get('id')
           ##     use.name = request.POST.get('name')
           ##     use.insurance = request.POST.get('insurance')
            ##    use.password = request.POST.get('password')
            ##    use.save()
             ##   return redirect('/dashboard', alert_flag='True'
    
  
  
  
  
  
  
    def post(self, request):
             ##deletet
             if request.POST.get('delete') == 'user':
                key = request.POST.get('Userkey')
                delDoctor = User.objects.get(user_id = key)
                delDoctor.delete()
                messages.success(self.request, 'Deleted Succesfully!')
                return redirect('/products')
        
             if request.POST.get('edit') == 'users':
                        edit_key = request.POST.get('edit_id')
                        editProduct = User.objects.get(user_id= edit_key)
                        editProduct.firstname = request.POST.get('firstname')
                        editProduct.lastname = request.POST.get(
                                     'lastname')
                        editProduct.phoneNumber = request.POST.get('contact')
                        editProduct.save()
                        messages.success(self.request, 'Edited successfully!')
                        return redirect('/products')

    def get(self,request):
        products = Products.objects.all()
        users = User.objects.all
        context = {

                 'products': products,
                  'users':   users
        }
        storage = messages.get_messages(request)
        for _ in storage:
            # This is important
            # Without this loop `_loaded_messages` is empty
            pass

       
        return render(request, 'products.html',context)
        
class AddProductView(View):
      def get(self,request):
            return render(request,'registerProducts.html')


