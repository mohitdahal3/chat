from django.shortcuts import render , HttpResponse , redirect 
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from chat.models import Room , Message
from django.core import serializers
import json
# Create your views here.
def home(request):
   return render(request , 'home.html')


def handlelogin(request):
   if request.method == "POST":
      uname = request.POST.get('lusername' , '')
      password1 = request.POST.get('lpassword' , '')
      user = authenticate(username = uname , password = password1)
      if user is not None:
         login(request , user)
         messages.success(request , "Login successful!")
         return redirect('/')
      else:
         messages.error(request , "Login failed. Try using different keywords!")
         return redirect('/')
   return HttpResponse('page not found')


def handlesignup(request):
   if request.method == "POST":
      uname = request.POST.get('suname' , '')
      pass1 = request.POST.get('spass1' , '')
      pass2 = request.POST.get('spass2' , '')
      if pass1 != pass2:
         messages.error(request , "Passwords did not match!")
         return redirect('/')
      else:
         user = User.objects.create_user(username=uname , password=pass1)
         user.save()
         login(request , user)
         messages.success(request , "Signed up successfully!")  
         return redirect('/')
   return HttpResponse('page not found')

def handlelogout(request):
   logout(request)
   messages.warning(request , "You are successfully logged out!")
   return redirect('/')   


def room(request , roomname , username):
   rome = Room.objects.get(name = roomname)
   user = User.objects.get(username = username)
   all_messages = Message.objects.filter(room = rome)
   return render(request , 'room.html' ,{'room':rome , 'user':user , 'messages':all_messages})   

def checkroom(request):
   if request.method == "POST":
      roomname = request.POST.get('room' , '')
      username = request.POST.get('user','')   
      
      if Room.objects.filter(name=roomname).exists():
         return redirect(f'/room/{roomname}&{username}/')

      else:
         newroom = Room(name = roomname)
         newroom.save()
         return redirect(f'/room/{roomname}&{username}/')
   return HttpResponse('page not found')      



def send(request):
   username = request.POST.get('username' , '')
   message = request.POST.get('message' , '')
   room_name = request.POST.get('roomname' , '')
   print(username ," hello world! " , message , room_name)
   got_room = Room.objects.get(name=room_name)
   new_message = Message(message = message  , user = User.objects.get(username = username),username = username, room = got_room)
   new_message.save()
   return HttpResponse(new_message)


def getMessages(request , roomname):
   room_object = Room.objects.get(name = roomname)
   all_messages = Message.objects.filter(room = room_object)
   
   return JsonResponse(list(all_messages.values()) , safe=False)