from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('profile', views.ProfileViewSet)
router.register('hitter', views.HitterRecordViewSet)
router.register('pitcher', views.PitcherRecordViewSet)
router.register('group', views.GroupViewSet)
router.register('permission', views.PermissionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name="rest_framework")
]
