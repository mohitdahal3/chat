from django.urls import path
from . import views

urlpatterns = [
   path('' , views.home , name = "home"),
   path('login/' , views.handlelogin , name = "login"),
   path('signup/' , views.handlesignup , name = "signup"),
   path('logout/' , views.handlelogout , name = "logout"),
   path('room/<str:roomname>&<str:username>/' , views.room , name = "room"),
   path('checkroom/' , views.checkroom , name = "checkroom"),
   path('send/' , views.send , name = "send"),
   path('getMessages/<str:roomname>/' , views.getMessages , name = "getMessages"),
]