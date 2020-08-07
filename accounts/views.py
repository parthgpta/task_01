from django.shortcuts import render , redirect
from .forms import Userprofile , Userform
from django.contrib.auth import  authenticate,login
from django.shortcuts import get_object_or_404
from .serializers import usercreateserializer ,getdetailserializer ,geteventdetail ,UserSerializer,createevent
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import  User
from .models import event



def home(request):
	 return render(request , 'home.html' ,{})


class create_user_serializer(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = usercreateserializer


class get_userdetails_serializer(ListAPIView):	
	permission_classes = (IsAuthenticated,)	
	serializer_class = getdetailserializer
	def get_queryset(self):
		return {self.request.user}


class update_user_serializer(UpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticated,)
	def patch(self , request ,*args , **kwargs):
		return self.partial_update(request ,*args ,**kwargs)

		
class get_event_details(ListAPIView):
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		if self.request.user.is_authenticated:
			return event.objects.filter(user=self.request.user)
		else:
			return (serializers.errors)

	serializer_class = geteventdetail

class create_events_serializer(CreateAPIView):
	permission_classes = (IsAuthenticated ,)
	queryset = event.objects.all()
	serializer_class = createevent

	def create(self,request,*args,**kwargs):
		event = createevent(data = request.data)
		if event.is_valid():
			event.save(user = self.request.user)			
		return Response(status=204)

	

class update_events_serializer(UpdateAPIView):
	permission_classes = (IsAuthenticated ,)
	queryset = event.objects.all()
	serializer_class = geteventdetail

	def patch(self , request , *args , **kwargs):
		return self.partial_update(request , *args , **kwargs)

class delete_events_serializer(RetrieveUpdateDestroyAPIView):
	serializer_class = geteventdetail
	queryset = event.objects.all()
	event  =None

	def delete(self, request , *args  ,**kwargs):
		self.event = get_object_or_404(event  ,pk=kwargs['pk'])
		self.event.delete()
		return Response("Event deleted",status=status.HTTP_201_CREATED)
