from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import cache_control
from .models import *
# Create your views here.

@cache_control(no_cache=True, must_validade=True, no_store=True)
def home(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']


        if User.objects.get(email=username):
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Log in Successful.')
                return HttpResponseRedirect('/') 

            else:
                messages.error(request, 'Wrong password or username')
                return HttpResponseRedirect('/') 
        else:
            messages.error(request, 'No user found. Register first')
            return HttpResponseRedirect('/registeration') 

            
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')
    
def team(request):
    return render(request, 'team.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['contact-email']
        message = request.POST['message']

        data = Contact(Name=name, Email=email, Message=message)
        data.save()
        messages.success(request, 'Message sent successfully.')
        return HttpResponseRedirect('/') 
    
def registeration(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        prn = request.POST['prn']
        branch = request.POST['branch']
        year = request.POST['year']
        password = request.POST['password']

        if fname == '':
            messages.error(request, 'Please enter first name')
            return HttpResponseRedirect('/registeration') 
        if lname == '':
            messages.error(request, 'Please enter last name')
            return HttpResponseRedirect('/registeration')
        if email == '':
            messages.error(request, 'Please enter Email-id')
            return HttpResponseRedirect('/registeration')
        if email in User.objects.filter(email=email):
            messages.error(request, 'Email user already exist')
            return HttpResponseRedirect('/')
        if password == '':
            messages.error(request, 'Please enter password')
            return HttpResponseRedirect('/registeration')
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 character long')
            return HttpResponseRedirect('/registeration')
        if not any(i.isupper() for i in password):
            messages.error(request, 'Password must contain at least one upper case letter')
            return HttpResponseRedirect('/registeration')
        if not any(i.islower() for i in password):
            messages.error(request, 'Password must contain at least one lower case letter')
            return HttpResponseRedirect('/registeration')
        if not any(i.isdigit() for i in password):
            messages.error(request, 'Password must contain at least one digit')
            return HttpResponseRedirect('/registeration')


        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = fname 
        user.last_name = lname
        user.save()
        
        data = Student(Student=user, Mobile=phone, PRN=prn, Branch=branch, Year=year)
        data.save()
        messages.success(request, 'Account has been created.')
        return HttpResponseRedirect('/')

    return render(request, 'register.html')


def profile(request):
    data = Student.objects.get(Student=request.user)
    return render(request, 'profile.html', {'student' : data })

def edit(request):
    data = Student.objects.get(Student=request.user)
    if request.method=='POST':
        user = Student.objects.get(Student=request.user)
        user.Phone = request.POST['phone']
        user.PRN = request.POST['prn']
        user.Branch = request.POST['branch']
        user.Year = request.POST['year']
      
        user.save()
        messages.success(request, 'Details updated.')
        return HttpResponseRedirect('/')

    return render(request, 'edit.html', {'student' : data })

def coding(request):
    if CodingProfile.objects.filter(Coder=request.user):
        data = CodingProfile.objects.get(Coder=request.user)
    else:
        data = None
    if request.method=='POST':
        leet = request.POST['leetcode']
        git = request.POST['github']
        hack = request.POST['hackerrank']
        linkedin = request.POST['linkedin']
        data = CodingProfile(Coder=request.user, Leetcode=leet, Github=git, Hackerrank=hack, Linkedin=linkedin)
        data.save()
        messages.success(request, 'Updated to Profile.')
        return HttpResponseRedirect('/CodingProfile')

    return render(request, 'coding.html', {'Coder' : data})

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def logoutuser(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return HttpResponseRedirect('/')
