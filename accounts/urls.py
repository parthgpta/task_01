from django.urls import path , include 
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns= [
	path('', views.home , name = 'home'),
    path('api/createuser/' , views.create_user_serializer.as_view(),name= 'createuserapi'),
    path('api/userdetails/' , views.get_userdetails_serializer.as_view(),name= 'createuserapi'),
    path('api/eventdetails/' , views.get_event_details.as_view(),name= 'geteventapi'),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/update/userdetails/<int:pk>/' ,views.update_user_serializer.as_view()),
    path('api/update/events/<int:pk>/' , views.update_events_serializer.as_view()),
    path('api/delete/events/<int:pk>/' , views.delete_events_serializer.as_view()),
    path('api/create/events/' , views.create_events_serializer.as_view()),
    
]