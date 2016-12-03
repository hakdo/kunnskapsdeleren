from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vestrerosten/$', views.vestrerosten, name='vestrerosten'),
    ]
