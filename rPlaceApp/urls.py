from django.conf.urls import url
from rPlaceApp import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
	url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^tiles/$', views.TileList.as_view(), name = 'tile-list'),
	url(r'^tiles/(?P<pk>[0-9]+)/$', views.TileDetail.as_view(), name = 'tile-detail'),
	url(r'^users/$', views.UserList.as_view(), name = 'user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name = 'user-detail'),
	url(r'^users/canplace/$', views.CanPlaceList.as_view()),
	url(r'tiles/map', views.GetMap.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)