from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
"""
def home(request):
    return HttpResponse('welcome to my website')

def room(request) :
    return HttpResponese('welcome to room')   
"""
rooms = [
    {'id':1,'name':'i am shivansh sharma'},
    {'id':2,'name':'i am a data scientist'},
    {'id':3,'name':'i am a programmer'}
    ]
def home(request):
    return render(request,'app/home.html',{'rooms':rooms}) #we can also do this by calling app/template
    #return render(request,'home.html') ,we can also call home.html from root template folder 

def room(request,pk):
    
    return render(request,'app/room.html')