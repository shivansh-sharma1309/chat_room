# i created 
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('CreateRoom/',views.CreateRoom,name='CreateRoom'),
    path('room/<str:pk>/',views.room,name='room'),
    path('updateRoom/',views.updateRoom,name='updateRoom'),
    path('deleteRoom/<str:pk>/',views.deleteRoom,name='deleteRoom'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('register/',views.registeruser,name='register')
]
