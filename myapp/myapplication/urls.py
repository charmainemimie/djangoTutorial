from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index') #index is a function found in views.py
]