from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from core.views import ListViewSet
# from rest_framework.authtoken import views 
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'list', ListViewSet, basename='list')
# router.register(r'item', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
