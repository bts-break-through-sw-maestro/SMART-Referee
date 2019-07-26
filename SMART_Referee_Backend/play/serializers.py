from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers
from .models import Play


class PlaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Play
        fields = '__all__'
