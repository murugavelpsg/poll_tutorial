from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('polls.views',
    url(r'^$','index'),
    url(r'^(?P<poll_id>\d+)/$','detail'),
    url(r'^(?P<poll_id>\d+)/results/$','results'),
    url(r'^(?P<poll_id>\d+)/vote/$','vote'),
    url(r'^(?P<poll_id>\d+)/ajaxvote/$', 'ajax_vote')
)
