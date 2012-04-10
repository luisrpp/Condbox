from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Home
    (r'^$', direct_to_template, {'template': 'index.html'}),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # User profile
    url(r'^accounts/profile/$', 'condbox.core.views.profile', name='profile'),
    # Logout using django.contrib.auth
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    # Django-registration
    (r'^accounts/', include('registration.urls')),
    # Core app
    (r'^', include('condbox.core.urls', namespace='core')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
else:
    # Defining URL mapping in the static files for environment Heroku
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {
            'document_root': settings.STATIC_ROOT,
            'insecure': True}),
    )
