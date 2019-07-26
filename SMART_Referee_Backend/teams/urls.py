from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from teams import views

router = routers.DefaultRouter()
router.register('teams', views.TeamsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
