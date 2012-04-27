from django.conf.urls.defaults import *

urlpatterns = patterns('shivsutra.views',
                       (r'^js/$', 'js'),
                       (r'^$', 'default'),

                       )
