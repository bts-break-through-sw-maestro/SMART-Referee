from django.contrib.auth.models import User, Permission
from rest_framework import viewsets
from .models import Profile, HitterRecord, PitcherRecord
import users.serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = users.serializers.UserSerializer
    

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = users.serializers.ProfileSerializer
    
    
class HitterRecordViewSet(viewsets.ModelViewSet):
    queryset = HitterRecord.objects.all()
    serializer_class = users.serializers.HitterSerializer
    
    
class PitcherRecordViewSet(viewsets.ModelViewSet):
    queryset = PitcherRecord.objects.all()
    serializer_class = users.serializers.PitcherSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = users.serializers.PermissionSerializer
