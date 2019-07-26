from django.shortcuts import render
from rest_framework import viewsets
from .models import Teams
import teams.serializers

class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = teams.serializers.TeamsSerializer
