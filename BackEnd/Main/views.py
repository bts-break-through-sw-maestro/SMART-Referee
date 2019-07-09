from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TestSerializer
from .models import Test

# Create your views here.

def index(request):
    return render(request, "index.html")

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
