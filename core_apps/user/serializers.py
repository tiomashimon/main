from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserActivity

class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class UserActivitySeralizer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'