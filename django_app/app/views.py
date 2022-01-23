from django.shortcuts import render
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

from .models import Room


def home(request):
    rooms = Room.objects.all()
    return render(request,'app/home.html',{'rooms':rooms}) #we can also do this by calling app/template
    #return render(request,'home.html') ,we can also call home.html from root template folder 

def room(request,pk):
    rooms = Room.objects.get(id=int(pk))
    """for i in rooms:
        if i['id'] == int(pk):
            Room = i['name']
            break"""
    context = {'room':rooms}
    return render(request,'app/room.html',context)