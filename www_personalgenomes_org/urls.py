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

    # About pages

    url(r'^about-us/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/about-us.html'),
        name='about-us'),
    url(r'^about.html/?$', ReverseRedirectView.as_view(url='about-us')),
    url(r'^people.html/?$', ReverseRedirectView.as_view(url='about-us')),

    url(r'^mission/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/mission.html'),
        name='mission'),
    url(r'^mission.html/?$', ReverseRedirectView.as_view(url='mission')),

    url(r'^press/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/press.html'),
        name='press'),
    url(r'^news.html/?$', ReverseRedirectView.as_view(url='press')),

    url(r'^publications/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/publications.html'),
        name='publications'),

    # Participate pages

    url(r'^pgp/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/pgp.html'),
        name='pgp'),
    url(r'^project.html/?$', ReverseRedirectView.as_view(url='pgp')),

    url(r'^why-participate/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/why-participate.html'),
        name='why-participate'),
    url(r'^whyparticipate.html/?$', ReverseRedirectView.as_view(url='why-participate')),

    url(r'^non-anonymous/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/non-anonymous.html'),
        name='non-anonymous'),

    # Global network pages

    url(r'^network/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/network.html'),
        name='network'),
    url(r'^international.html/?$', ReverseRedirectView.as_view(url='network')),

    url(r'^join-network/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/join-network.html'),
        name='join-network'),

    url(r'^harvard/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/harvard.html'),
        name='harvard'),

    url(r'^mclaughlin-centre/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/mclaughlin-centre.html'),
        name='mclaughlin-centre'),

)
