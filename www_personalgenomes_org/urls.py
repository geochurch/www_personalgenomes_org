from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from .views import redirect_to_name

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
    url(r'^about.html/?$', redirect_to_name, {'url_name': 'about-us'}),

    url(r'^mission/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/mission.html'),
        name='mission'),
    url(r'^mission.html/?$', redirect_to_name, {'url_name': 'mission'}),

    url(r'^people/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/people.html'),
        name='people'),
    url(r'^people.html/?$', redirect_to_name, {'url_name': 'people'}),

    url(r'^press/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/press.html'),
        name='press'),
    url(r'^news.html/?$', redirect_to_name, {'url_name': 'press'}),

    url(r'^publications/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/publications.html'),
        name='publications'),

    # Participate pages

    url(r'^pgp/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/pgp.html'),
        name='pgp'),
    url(r'^project.html/?$', redirect_to_name, {'url_name': 'pgp'}),

    url(r'^why-participate/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/why-participate.html'),
        name='why-participate'),
    url(r'^whyparticipate.html/?$', redirect_to_name, {'url_name': 'why-participate'}),

    url(r'^non-anonymous/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/non-anonymous.html'),
        name='non-anonymous'),

    url(r'^risks-benefits/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/risks-benefits.html'),
        name='risks-benefits'),
    url(r'^considerations.html/?$', redirect_to_name, {'url_name': 'risks-benefits'}),

    url(r'^pgp-sign-up/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/pgp-sign-up.html'),
        name='pgp-sign-up'),
    url(r'^eligibility.html/?$', redirect_to_name, {'url_name': 'pgp-sign-up'}),

    # Research pages

    url(r'^data/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/data.html'),
        name='data'),

    url(r'^sharing/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/sharing.html'),
        name='sharing'),
    url(r'^sharing.html/?$', redirect_to_name, {'url_name': 'sharing'}),

    # Global network pages

    url(r'^network/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/network.html'),
        name='network'),
    url(r'^international.html/?$', redirect_to_name, {'url_name':'network'}),

    url(r'^join-network/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/join-network.html'),
        name='join-network'),

    url(r'^harvard',
        include('harvard.urls', namespace="harvard")),
    url(r'^mclaughlin_centre/?$',
        include('mclaughlin_centre.urls', namespace="mclaughlin_centre")),

)
