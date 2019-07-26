from django.shortcuts import render
from rest_framework import viewsets
from .models import Play
import play.serializers

class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = play.serializers.PlaySerializer
