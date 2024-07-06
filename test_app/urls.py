from django.contrib import admin
from django.urls import path

from test_app.views import index,template_test,manyshop

urlpatterns = [
    path('index/',index),
    path('template',template_test),
    path('<int:city_id>/<int:shop_id>/',manyshop),
]
