from datetime import datetime, timedelta
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import SingUpSerializers,UserSerializers
from django.core.mail import send_mail

from django.utils.crypto import get_random_string
# Create your views here.

@api_view(['POST'])
def register(request):
   data = request.data
   user = SingUpSerializers(data=data)
   if user.is_valid():
      if not User.objects.filter(username=data['email']).exists() :
         user = User(
            username = data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=make_password(data['password']) , 
         )
         user.save()
         return Response({'details':"Your account registered successfuly !"},status=status.HTTP_201_CREATED)
      else :
         return Response({'details':"This email already exists !"},status=status.HTTP_400_BAD_REQUEST)
   else :
      return Response(user.errors)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
   user = UserSerializers(request.user,many=False)
   return Response(user.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
   user = request.user
   data = request.data 

   user.first_name = data['first_name']
   user.last_name = data['last_name']
   user.username = data['email']
   user.email = data['email']

   if user.password !=  "":
      user.password = data['password']
   
   user.save()
   ser = UserSerializers(user,many=False)
   return Response(ser.data)

@api_view(['POST'])
def forgot_password(request):
   data = request.data
   user = get_object_or_404(User, email=data['email'])
   token = get_random_string(40)
   expire_date = datetime.now() + timedelta(minutes=30)
   user.reset_password_token = token
   user.reset_password_expire = expire_date
   user.save()

   link= "http://127.0.0.1:8000/api/reset_password/{token}".format(token = token)
   body = "Your Password reset link is : {link}".format(link=link)
   send_mail("Password reset eMarket",body, "eMarket@eMarket.dz",[data['email']])

   return Response({'details':'Password reset sent to {email}'.format(email=data['email'])})

@api_view(['POST'])
def reset_password(request,token):
   data = request.data
   user = get_object_or_404(User, profile__reset_password_token = token)
   if user.Profile.reset_password_expire.replace(tzinfo=None) < datetime.now() : 
      return Response({'error':'Token is expi red'},status=status.HTTP_400_BAD_REQUEST)
   
   if data['password'] != data['confirmPassword'] :
      return Response({'error':'Password are not same'},status=status.HTTP_400_BAD_REQUEST)
   
   user.password = make_password(data['password'])
   user.Profile.reset_password_token = ""
   user.reset_password_expire = None
   user.Profile.save()
   user.save()
   return Response({'details':'Password reset done'})