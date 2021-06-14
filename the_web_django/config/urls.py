from django.contrib import admin
from django.urls import path

from core.views import (
    index,
    IndexView,
    SubscriberAPIView,
    ProfileAPIView,
)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('index-view/', IndexView.as_view()),
    path('subscriber-view/', SubscriberAPIView.as_view()),
    path('profile-view/', ProfileAPIView.as_view()),
]
