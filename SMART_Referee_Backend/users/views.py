from django.contrib.auth.models import User, Group, Permission
from rest_framework import viewsets
from .models import Profile
import users.serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = users.serializers.UserSerializer
    

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = users.serializers.ProfileSerializer
    
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = users.serializers.GroupSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = users.serializers.PermissionSerializer
