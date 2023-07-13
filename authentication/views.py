from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_page(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['psw']

            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return redirect('/home')
                else:
                    messages.error(request, "Incorrect password!")
            else:
                messages.error(request, "Unknown email, please sign up first!")
                return redirect('/signup')

        return render(request, 'login.html')

    return redirect('/home')


# def login_page(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['psw']
#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             # Authentication successful
#             print("hi")
#             login(request, user)
#             return redirect('home')  # Redirect to the home page
#         else:
#             # Authentication failed
#             print("invalid")
#             error_message = "Invalid email or password. Please try again."
#             return render(request, 'login.html', {'error_message': error_message})

#     return render(request, 'login.html')

# def login_page(request):
    
#     if not request.user.is_authenticated:      
#         if request.method == 'POST':
#             email = request.POST['email']
#             password = request.POST['psw']
#             user = authenticate(request, email=email, password=password)
            
#             if User.objects.filter(email=email).exists():
#                 user = User.objects.get(email=email)
#                 if user.check_password(password):
#                     print(user)
#                     login(request, user)
#                     print("done")
#                     return redirect('/home')
#                 else:
#                     messages.error(request, "Incorrect password!")
#             else:
#                 messages.error(request, "Unknown email, please signup first!")
#                 return redirect('/login')

#         return render(request, 'login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'logout.html')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            # Use the email's username
            username = email.split('@')[0]
            password1 = request.POST['psw']
            password2 = request.POST['psw-repeat']
            
            if User.objects.filter(email=email):
                messages.error(request, "Emali already registered!")
                return redirect('/signup')
                        
            if password1 != password2:
                messages.error(request, "Password didn't match!")
                return redirect('/signup')

            newuser = User.objects.create_user(username, email, password1, first_name=fname, last_name=lname)
            newuser.is_active = False
            newuser.save()
            messages.success(request, "Your Account has been successfully created.")
            return redirect('/')
    return render(request, "signup.html")