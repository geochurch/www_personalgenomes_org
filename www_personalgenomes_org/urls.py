from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

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

    (r'^$', TemplateView.as_view(template_name='www_personalgenomes_org/index.html')),

    # Global network pages
    (r'^international.html', TemplateView.as_view(template_name='www_personalgenomes_org/network.html')),
    (r'^network(.html|/|)$', TemplateView.as_view(template_name='www_personalgenomes_org/network.html')),
    (r'^start-pgp(.html|/|)$', TemplateView.as_view(template_name='www_personalgenomes_org/start-pgp.html')),

    # About pages
    (r'^mission(.html|/|)$', TemplateView.as_view(template_name='www_personalgenomes_org/mission.html')),

)
