from asyncore import write
from django.urls import path

from . views import *

urlpatterns = [
    path('', writers, name='main-page'),
    path('<int:name>', quote_by_number),
    path('<str:name>', quote, name='writer-quote')
]
