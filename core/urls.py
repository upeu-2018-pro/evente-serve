
from django.conf.urls import url, include
from rest_framework import routers
from .views.user_view import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

from .views.localuserinfo_view import LocalUserInfoView

urlpatterns = [

    url(r'^localuserinfo/$', LocalUserInfoView.as_view()),
    url(r'^', include(router.urls)),
]
