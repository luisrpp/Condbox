from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('condbox.core.views',
    url(r'^search_condo/$', 'search_condo', name='search_condo'),
    url(r'^condo_results/$', 'ajax_condo_search', name='ajax_condo_search'),
    url(r'^condo/(?P<slug>[\w_-]+)/$', 'condo', name='condo'),
    url(r'^condo/(?P<slug>[\w_-]+)/add_dweller/$', 'add_dweller', name='dweller'),
)
