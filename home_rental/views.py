from django.shortcuts import render, redirect,get_object_or_404

from .models import AddRentalHome
from .forms import AddRentalHomeForm
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm


from django.db.models import Q



def homepage(request):
    q = request.GET.get('q', '')
    sort_order = request.GET.get('sort', '')

    if q:
        multiple_q = Q(Q(City__icontains=q) | Q(Street2__icontains=q))
        homedata = AddRentalHome.objects.filter(multiple_q)
    else:
        homedata = AddRentalHome.objects.all()

    if sort_order == 'asc':
        homedata = homedata.order_by('Rent')  
    elif sort_order == 'desc':
        homedata = homedata.order_by('-Rent')
    return render(request, "home.html", {
        'homedata': homedata
    })


def about(request):
    return render(request,"about.html")


from django.shortcuts import render, redirect
from .forms import AddRentalHomeForm

def add_home(request):
    if request.method == 'POST':
        form = AddRentalHomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')  
        else:
            print(form.errors)  
    else:
        form = AddRentalHomeForm()

    return render(request, 'add_home.html', {'form': form})


def detail_page(request,slug):
    identified_post=get_object_or_404(AddRentalHome, slug=slug)
    return render(request,"detail_page.html",{
        "home_detail":identified_post,
        
    })

    
def signin_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = SignupForm()
    return render(request, 'signin.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('login')