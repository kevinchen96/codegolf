from django.conf.urls import patterns, url

urlpatterns = patterns('',
        url(r'add/$', 'problem.views.add_problem'),
)
