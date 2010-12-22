from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^edit/(?P<model_app>\w+)/(?P<model_name>\w+)/(?P<object_id>\d+)/$',
            'jeditable.views.edit'),
)
