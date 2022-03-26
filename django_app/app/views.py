from django.shortcuts import render , redirect
# Create your views here.

from django.http import HttpResponse
"""
def home(request):
    return HttpResponse('welcome to my website')

def room(request) :
    return HttpResponese('welcome to room')   
"""
"""rooms = [
    {'id':1,'name':'i am shivansh sharma'},
    {'id':2,'name':'i am a data scientist'},
    {'id':3,'name':'i am a programmer'}
    ]
"""

from .models import Room , Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
def loginuser(request):

    page = 'login'

    if request.user.is_authenticated :
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        username = username.lower()
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect('home')
        else :
            messages.error(request,'incorrect username or password!')    
    context = {'page':page}
    return render(request,'app/login.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def registeruser(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        exist_user = User.objects.get(username = request.user.username.lower())
        if exist_user != None :
            messages.error(request,'Please try again')
        if form.is_valid():
            user = form.save(commit=False) #we perform cleaning of entered data before submitting it .
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else :
            messages.error(request,'user already exist ')    
            return redirect('register')
    context = {'page':page , 'form':form}
    return render(request,'app/login.html',context)

def home(request):
    
    if request.GET.get('q') != None :
        q = request.GET.get('q') 
    else :
        q = ''
    if q != '':
        # for room search
        room = Room.objects.filter(Q(name__icontains=q) | Q(topic__name__icontains=q) | Q(description__icontains=q) | Q(host__username__icontains=q))
        topic = Topic.objects.all()
    else :
        room = Room.objects.all()
        topic = Topic.objects.all()
    context = {'rooms' : room , 'topics' : topic,'name':User.username}
    return render(request,'app/home.html',context)
     #we can also do this by calling app/template
    #return render(request,'home.html') ,we can also call home.html from root template folder 

def room(request,pk):
    rooms = Room.objects.get(id=pk)
    if request == "POST":
        message = request.POST.get('message')
    """for i in rooms:
        if i['id'] == int(pk):
            Room = i['name']
            break"""
    context = {'room':rooms}
    return render(request,'app/room.html',context)

@login_required(login_url='login')
def CreateRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'Form':form}
    return render(request,'app/room_form.html',context)

@login_required(login_url='login')
def updateRoom(request):
    if request.method == 'POST':
        room = Room.objects.get(id = request.GET.get('ID',None))
        form = RoomForm(request.POST,instance=room)
        form.save()
        return redirect(home)
    if request.GET.get('ID') != None:
        room = Room.objects.get(id = request.GET.get('ID'))
        if request.user != room.host or request.user == request.user.is_superuser:
            return HttpResponse('you are not allowed to perform this action')
        form = RoomForm(instance = room)
        context = {'Form' : form}
        return render(request,'app/room_form.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        if request.user != room.host or request.user == request.user.is_superuser:
            return HttpResponse('you are not allowed to perform this action')
        room.delete()
        return redirect(to='home')
    return render(request,'app/delete.html',context={'obj':room})


