from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/',  admin.site.urls),
    url(r'^beta/$', views.beta, name='beta'),
    url(r'^nyttpassord/$', views.changepassword, name='changepassword'),
]
