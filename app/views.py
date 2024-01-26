from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from app.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from app import models
from .forms import *



# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)



def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password incorrect')
    return render(request, 'login.html')



def logout_func(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def filter(request, item):
    properties = filter_search(item)
    return properties



def booking(request, name):
    booked = booking_props(name)
    context = {'booked':booked}
    return render(request, 'userpage.html',context)



def homepage(request):
    if request.POST:
        if 'filterbtn' in request.POST:
            item = request.POST.get('filter')
            places = filter(request, item)
            context = {'places': places}
            return render(request, 'home.html', context)
    else:
        places = Properties.objects.all()
        context = {'places': places}
        return render(request, 'home.html', context)



@login_required(login_url='login')
def userpage(request):
    form = CreateAccount(initial={'user': request.user})
    if request.method == 'POST':
        if 'delete_property' in request.POST:
            property_id = request.POST['delete_property']
            property_to_delete = get_object_or_404(Properties, id=property_id, user_props=request.user.account)
            property_to_delete.delete()
            return redirect('user')
        if 'prop_sold' in request.POST:
            property_id = request.POST['prop_sold']
            property_to_sale = get_object_or_404(Properties, id=property_id, user_props=request.user.account)
            if property_to_sale.available == True:
                property_to_sale.available = False
                property_to_sale.save()
                return redirect('user')
            if property_to_sale.available == False:
                property_to_sale.available = True
                property_to_sale.save()
                return redirect('user')
        if 'create_account' in request.POST:
            form = CreateAccount(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('user')
            else:
                return redirect('home')
            
        else:
            user = request.user
            try:
                account = Account.objects.get(user = user.id)
                places = Properties.objects.filter(user_props = account)
            except Account.DoesNotExist:
                account = None
                places = None
            context = {'account': account, 'places': places, 'user': user}
            return render(request, 'userpage.html', context)
    else:
        user = request.user
        try:
            account = Account.objects.get(user = user.id)
            places = Properties.objects.filter(user_props = account)
        except Account.DoesNotExist:
            account = None
            places = None
        context = {'account': account, 'places': places, 'user': user, 'form': form}
        return render(request, 'userpage.html', context)



@login_required(login_url='login')
def add_property(request):
    form = AddProperty(initial={"user_props": request.user.account})
    if request.method == 'POST':
        form = AddProperty(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('user')
    else:
        context = {'form': form}
        return render(request, 'add_property.html', context)

