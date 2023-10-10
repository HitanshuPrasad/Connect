from django.contrib.auth.models import User
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Clients,Professionals
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from datetime import datetime
# Create your views here.


# LOGIN VIEW FOR CLIENT BABY
def login_client(request):
    if request.user.is_authenticated:
        return redirect(home_client)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect(home_client)
    return render(request,'login_client.html')




# LOGIN VIEW FOR PROFESSIONAL BABY
def login_professional(request):
    if request.user.is_authenticated:
        return redirect(home_professional)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect(home_professional)
    return render(request,'login_professional.html')


# CREATE PROFILE AND CLIENT SIGNUP VIEW BABY
def signup_client(request):
    if request.user.is_authenticated:
        return redirect(home_client)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        city = request.POST['city']
        image=request.POST['image']
        user = User.objects.create_user(username=username,password=password)
        client = Clients.objects.create(user=user,email=email,city=city,joining_date=datetime.today(),profile_picture=image)
        if client:
            messages.success(request,'Profile Created Please Login')
            return redirect(home_client)
    return render(request,'signup_client.html')


def signup_professional(request):
    if request.user.is_authenticated:
        return redirect(home_professional)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        city = request.POST['city']
        profession = request.POST['profession']
        skills = request.POST['skills']
        image=request.POST['image']
        user = User.objects.create_user(username=username,password=password)
        professional = Professionals.objects.create(user=user,email=email,city=city,profession=profession,skills=skills,joining_date=datetime.today(),profile_picture=image)
        if professional:
            messages.success(request,'Profile Created Please Login')
            return redirect(home_professional)
    return render(request,'signup_professional.html')




# FOR RENDERING THE PROFILE PAGE
def profile_client(request,id=None):
    if not request.user.is_authenticated:
        return redirect(index)
    profile_id = Clients.objects.get(user=request.user)
    profile = Clients.objects.get(user=request.user)
    profileimage = profile.profile_picture.url
    return render(request,'profile_client.html',{'profile':profile_id,'profileimage':profileimage,'profile_of_user':True})


# FOR RENDERING THE PROFILE PAGE
def profile_professional(request,id=None):
    if not request.user.is_authenticated:
        return redirect(index)
    profile = Professionals.objects.filter(user=request.user).first()
    profileimage = profile.profile_picture.url
    return render(request,'profile_professional.html',{'profile':profile,'profileimage':profileimage,'profile_of_user':True})




def Logout(request):
    logout(request)
    return render(request,'index.html')



def home_client(request):
    if not request.user.is_authenticated:
        return render(request,'index.html')
    professionals= Professionals.objects.all()
    context = {"posts":professionals}
    return render(request,'home_client.html',context)



def home_professional(request):
    if not request.user.is_authenticated:
        return render(request,'index.html')
    clients= Clients.objects.all()
    context = {"posts":clients}
    return render(request,'home_professional.html',context)

def index(request):
    return render(request,"index.html")


def search_client(request):
    if not request.user.is_authenticated:
        return redirect(index)
    profile = Clients.objects.get(user=request.user)
    profileimage = profile.profile_picture.url
    search = request.GET['search']
    # lookups= Q(Professionals.user__username__icontaines=search)
    profiles = Professionals.objects.filter(Q(user__username__icontains=search) | Q(email__icontains=search) | Q(city__icontains=search) | Q(profession__icontains=search) | Q(skills__icontains=search))
    context = {'posts':profiles,'search':search,"profileimage":profileimage}
    return render(request,'search_client.html',context)

def search_professional(request):
    if not request.user.is_authenticated:
        return redirect(index)
    profile = Professionals.objects.get(user=request.user)
    profileimage = profile.profile_picture.url
    search = request.GET['search']
    profiles = Clients.objects.filter(Q(user__username__icontains=search) | Q(email__icontains=search) | Q(city__icontains=search) )
    context = {'posts':profiles,'username':search,"profileimage":profileimage}
    return render(request,'search_professional.html',context)
