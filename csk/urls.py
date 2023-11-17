from django.urls import path
from csk.views import *
from rcb.views import *
name='something'

urlpatterns = [
    path('msd/',msd,name='msd'),
    path('virat/',virat,name='virat'),
]