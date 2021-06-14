from django.contrib import admin
from django.urls import path

from rest_framework import routers

from core.views import (
    index,
    IndexView,
    SubscriberAPIView,
    ProfileViewSet,
)


router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('index-view/', IndexView.as_view()),
    path('subscriber-view/', SubscriberAPIView.as_view()),
]

urlpatterns += router.urls
