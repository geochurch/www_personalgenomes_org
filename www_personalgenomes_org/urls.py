from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from .views import ReverseRedirectView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'www_personalgenomes_org.views.home', name='home'),
    # url(r'^www_personalgenomes_org/', include('www_personalgenomes_org.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='www_personalgenomes_org/index.html')),

    # Global network pages
    url(r'^network(.html|/|)$', TemplateView.as_view(template_name='www_personalgenomes_org/network.html'), name='network'),
    url(r'^start-pgp(.html|/|)$', TemplateView.as_view(template_name='www_personalgenomes_org/start-pgp.html')),

    # About pages
    url(r'^mission(.html|/|)$', TemplateView.as_view(template_name='www_personalgenomes_org/mission.html')),

    # Redirects
    url(r'^international.html/$', ReverseRedirectView.as_view(url='network')),

)
