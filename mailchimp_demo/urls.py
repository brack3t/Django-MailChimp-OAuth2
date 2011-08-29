from django.conf.urls.defaults import patterns, include, url

from common.views import IndexView, ProfileView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'', include('banana_py.urls')),
    # Examples:
    # url(r'^$', 'mailchimp_demo.views.home', name='home'),
    # url(r'^mailchimp_demo/', include('mailchimp_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
