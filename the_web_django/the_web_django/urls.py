from django.contrib import admin
from django.urls import path

from core.views import index, IndexView

urlpatterns = [
    path('', index),
    path('index-view/', IndexView.as_view()),
    path('admin/', admin.site.urls),
]