from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.givetake, name='givetake'),
    url(r'^gt2/$', views.gt2, name='givetake2'),
    url(r'^give$', views.give, name='give'),
    url(r'^take$', views.take, name='take'),
    url(r'^details/(?P<pk>\d+)/$', views.details, name='details'),
    url(r'^p$', views.profile, name='profile'),
    url(r'^tag/(?P<pk>\d+)/$', views.tags, name='tags'),
    url(r'^news$', views.news, name='news'),
    url(r'^search$', views.search, name='search'),
    url(r'^groups/(?P<pk>\d+)/$', views.group, name='group'),
    url(r'^groups/(?P<pk>\d+)/$', views.group, name='group'),
    url(r'^groups/(?P<pk>\d+)/addtogroup/$', views.addtogroup, name='addtogroup'),
    url(r'^groups/(?P<pk>\d+)/addpeople/$', views.addpeople, name='addpeople'),
    url(r'^groups/addgroup/$', views.addgroup, name='addgroup'),
]
