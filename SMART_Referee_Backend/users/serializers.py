from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.HyperlinkedRelatedField(
        read_only=True, 
        view_name='UserViewSet',
        )
        
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
