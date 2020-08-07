from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import event


class UserSerializer(ModelSerializer):
	class Meta:
		model = User 
		fields = [
			'username',
			'password'
		]

class usercreateserializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'] ,
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User

        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email'
        ]

class getdetailserializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
			'id',
			'first_name',
			'last_name',
			'username',
			'email'
		]


class geteventdetail(ModelSerializer):

	def create(self  ,validated_data):
		
		# event = event.objects.create(
		# 	date=validated_data['date'],
  #           time=validated_data['time'],
  #           details = validated_data['details'],
  #           user = self.request.user
		# 	)
		# event.save()
		return event

	class Meta:
		model = event
		fields = [
			'id',
			'date' ,
			'time',
			'details'
		]

class createevent(ModelSerializer):
	class Meta:
		model = event
		fields = [
			'date' ,
			'time',
			'details'
		]




