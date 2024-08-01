from django.urls import path
from . import views

urlpatterns=[
    path('myFirst/',views.myFirst,name='myFirst'),
]