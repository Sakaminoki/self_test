from django.contrib import admin
from django.urls import path

from test_app.views import index,template_test

urlpatterns = [
    path('index/',index),
    path('template',template_test),
]
