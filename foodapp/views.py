from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import customerinfomodel, morningmenu, afternoonmenu, eveningmenu, orderinfo
from .forms import customerinfoform, dashboardform, dashboardformat, foodformat, TestForm, orderinfoform
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

from django.db.models import F

def home(request):
    return render(request, 'foodapp/home.html')


def register(request):
    form = customerinfoform()
    
    if request.method == 'POST':
        form = customerinfoform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'you have successfully registered')
            return redirect('logins')
    
    context = {'form':form}
    return render(request, 'foodapp/register.html', context)


def logins(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid username of password')
            return redirect('logins')
    return render(request, 'foodapp/logins.html')



def logoutuser(request):
    logout(request)
    return redirect('home')


def menu(request):
    sandry = morningmenu.objects.all() #morning
    follow = afternoonmenu.objects.all() #afternoon
    caliro = eveningmenu.objects.all() #evening

    context = {'sandry':sandry, 'follow':follow, 'caliro':caliro}
    return render(request, 'foodapp/menu.html', context)

def about(request):
    return render(request, 'foodapp/about.html')

def gallery(request):
    return render(request, 'foodapp/gallery.html')


def contact(request):
    return render(request, 'foodapp/contact.html')

def dashboard(request):
    dashshow = orderinfo.objects.all()
    context ={'dashshow':dashshow}
    return render(request, 'foodapp/dashboard.html', context)


def dashboardupdate(request):
    sandry = morningmenu.objects.all()
    follow = afternoonmenu.objects.all()
    caliro = eveningmenu.objects.all()

    dev = dashboardform()
    if request.method == "POST":
        dev = dashboardform(request.POST)
        if dev.is_valid():
            dev.save()
            return redirect('dashboardupdate')

    devo = dashboardformat()
    if request.method == "POST":
        devo = dashboardformat(request.POST)
        if devo.is_valid():
            devo.save()
            return redirect('dashboardupdate')

    dema = foodformat()
    if request.method == "POST":
        dema = foodformat(request.POST)
        if dema.is_valid():
            dema.save()
            return redirect('dashboardupdate')

    context = {'dev':dev, 'devo':devo, 'dema':dema, 'follow':follow, 'sandry':sandry, 'caliro':caliro}
    return render(request, 'foodapp/dashboardupdate.html', context)

def customerdatabase(request):
    piro = customerinfomodel.objects.all()

    context = {'piro':piro}
    return render(request, 'foodapp/customerdatabase.html', context)

def morningmenudelete(request,pk):
    fademu = morningmenu.objects.get(id=pk)
    if request.method == "POST":
        fademu.delete()
        return redirect('dashboardupdate')

    context={'fademu':fademu}
    return render(request, 'foodapp/morningmenudelete.html', context)


def afternoonmenudelete(request, pk):
    collit = afternoonmenu.objects.get(id=pk)

    if request.method == "POST":
        collit.delete()
        return redirect('dashboardupdate')
    
    context = {'collit':collit}
    return render(request, 'foodapp/afternoonmenudelete.html', context)

def eveningmenudelete(request, pk):
    lolip = eveningmenu.objects.get(id=pk)

    if request.method == "POST":
        lolip.delete()
        return redirect('dashboardupdate')

    return render(request, 'foodapp/eveningmenudelete.html', {'lolip':lolip})


def updatemenuitem(request, pk):
    fademu = morningmenu.objects.get(id=pk)

    don = dashboardform(instance=fademu)
    if request.method == "POST":
        don = dashboardform(request.POST, instance=fademu)
        if don.is_valid():
            don.save()
            return redirect('dashboardupdate')

    context = {'fademu':fademu, 'don':don}
    return render(request, 'foodapp/updatemenuitem.html', context)


def updatemenuafternoon(request, pk):#afternoon
    collit = afternoonmenu.objects.get(id=pk) 

    viks = foodformat(instance=collit)
    if request.method == "POST":
        viks = foodformat(request.POST, instance=collit)
        if viks.is_valid():
            viks.save()
            return redirect('dashboardupdate')
            
    context= {'collit':collit, 'viks':viks}
    return render(request, 'foodapp/updatemenuafternoon.html', context)

#for evening update
def updatemenuevening(request, pk):#evening
    lolip = eveningmenu.objects.get(id=pk)

    forn = dashboardformat(instance=lolip)
    if request.method == "POST":
        forn = dashboardformat(request.POST, instance=lolip)
        if forn.is_valid():
            forn.save()
        return redirect('dashboardupdate')

    context = {'lolip':lolip, 'forn':forn}
    return render(request, 'foodapp/updatemenuevening.html', context)


def orderpagemorning(request, pk):
    sandrys = morningmenu.objects.get(id=pk)

    num1 = int(sandrys.price)
    num2 = int(sandrys.quantity) #int(request.GET['num2'])
    result = num1 * num2
    

    scont = orderinfoform(instance=sandrys)
    if request.method == "POST":
        scont = orderinfoform(request.POST, instance=sandrys)
        if scont.is_valid():
            instance = scont.save(commit=False)
            instance.username = request.user
            instance.save()
        return redirect('menu')

    context = {'result':result,'scont':scont,'sandrys':sandrys}#
    return render(request, 'foodapp/orderpagemorning.html', context)



def dashboardentry(request):
    dashiboy = orderinfo.objects.all()

    context = {'dashiboy':dashiboy}
    return render(request, 'foodapp/dashboardentry.html', context) 


def menuordermorning(request, pk):
    return render(request, 'foodapp/menuordermorning.html')


def order(request):
    morningmenu = request.user.food_type
    order = order.objects.get_or_create(morningmenu=morningmenu, complete=False)
    items = morningmenu.order_set.all()

    context = {'morningmenu':morningmenu, 'order':order, 'items':items}
    return redirect(request, 'foodapp/order.html', context)















def sand(request):
    return render(request, 'foodapp/sand.html')

















