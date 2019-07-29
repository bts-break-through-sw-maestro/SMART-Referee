from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import play.urls, users.urls, teams.urls, records.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(users.urls)),
    path('api/', include(play.urls)),
    path('api/', include(teams.urls)),
    path('api/', include(records.urls)),
    path('api-auth/', include('rest_framework.urls'), name="rest_framework"),
]
