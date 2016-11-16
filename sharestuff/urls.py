from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.givetake, name='givetake'),
    url(r'^give$', views.give, name='give'),
    url(r'^take$', views.take, name='take'),
    url(r'^details/(?P<pk>\d+)/$', views.details, name='details'),
    url(r'^p$', views.profile, name='profile'),
    url(r'^tag/(?P<pk>\d+)/$', views.tags, name='tags'),
    url(r'^news$', views.news, name='news'),
    url(r'^search$', views.search, name='search'),
]
