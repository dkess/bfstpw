from django.conf.urls import patterns, url

from bfstpw import views

urlpatterns = patterns('',
    url(r'^$', views.threadlist, name='bfstpw-threadlist'),
    url(r'^(?P<thread_id>\d+)/$', views.thread, name='bfstpw-thread'),
    url(r'^(?P<thread_id>\d+)/post/$', views.post, name='bfstpw-post'),
    url(r'^newthreadmake/$', views.newthreadmake, name='bfstpw-newthreadmake'),
)
