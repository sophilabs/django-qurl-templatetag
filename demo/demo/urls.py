from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^', include('foo.urls', namespace='foo')),
                       )
