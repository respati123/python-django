from django.conf.urls import url
from . import views


app_name = "music"

urlpatterns = [


    url(r'^$', views.IndexViews.as_view(), name='index') ,
    url(r'^(?P<album_id>[0-9]+)/$', views.DetailViews.as_view(), name="detail"),
    url(r'album/add/$', views.AlbumCreate.as_view(), name="album-add")

]

