
from django.contrib import admin
from django.urls import path
from apk.views import *

urlpatterns = [
    path('', CrimeVideosView.as_view(),name='crime_view'),
]
