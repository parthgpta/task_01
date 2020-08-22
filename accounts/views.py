from django.shortcuts import render , redirect

from django.contrib.auth import  authenticate,login
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import  User



def home(request):
	return render(request , "home.html" , {})



