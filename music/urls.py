from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^music/$', views.index, name='index'),
    url(r'^forum/$', views.forum, name='forum'),
    # url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^music/(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^forum/(?P<album1_id>[0-9]+)/$', views.detail1, name='detail1'),
    url(r'^questions/(?P<album2_id>[0-9]+)/$', views.detail2, name='detail2'),
    # url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    # url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    # url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^forum/(?P<album1_id>[0-9]+)/my/$', views.detail3, name='detail3'),
    url(r'^forum/(?P<album1_id>[0-9]+)/new_question/$', views.create_song, name='create_song'),
    url(r'^forum/(?P<album1_id>[0-9]+)/delete_question/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    # url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    # url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]
