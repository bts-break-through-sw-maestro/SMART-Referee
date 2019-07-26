from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from play import views

router = routers.DefaultRouter()
router.register('play', views.PlayViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
