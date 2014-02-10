from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from . import views

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

    # Main page (location aware)
    url(r'^$', views.index, name='index'),

    # About pages

    url(r'^mission/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/mission.html'),
        name='mission'),
    url(r'^mission.html/?$', views.redirect_to_name, {'url_name': 'mission'}),
    url(r'^about.html/?$', views.redirect_to_name, {'url_name': 'mission'}),

    url(r'^people/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/people.html'),
        name='people'),
    url(r'^people.html/?$', views.redirect_to_name, {'url_name': 'people'}),

    url(r'^press/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/press.html'),
        name='press'),
    url(r'^news.html/?$', views.redirect_to_name, {'url_name': 'press'}),

    url(r'^publications/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/publications.html'),
        name='publications'),
    url(r'^research.html/?$', views.redirect_to_name, {'url_name': 'publications'}),

    # Participate pages

    url(r'^pgp/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/pgp.html'),
        name='pgp'),
    url(r'^project.html/?$', views.redirect_to_name, {'url_name': 'pgp'}),

    url(r'^why-participate/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/why-participate.html'),
        name='why-participate'),
    url(r'^whyparticipate.html/?$', views.redirect_to_name, {'url_name': 'why-participate'}),

    url(r'^non-anonymous/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/non-anonymous.html'),
        name='non-anonymous'),

    url(r'^risks-benefits/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/risks-benefits.html'),
        name='risks-benefits'),
    url(r'^considerations.html/?$', views.redirect_to_name, {'url_name': 'risks-benefits'}),

    url(r'^pgp-sign-up/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/pgp-sign-up.html'),
        name='pgp-sign-up'),
    url(r'^signup.html/?$', views.redirect_to_name, {'url_name':'pgp-sign-up'}),
    url(r'^eligibility.html/?$', views.redirect_to_name, {'url_name':'pgp-sign-up'}),

    # Research pages

    url(r'^get-data/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/get-data.html'),
        name='get-data'),

    url(r'^sharing/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/sharing.html'),
        name='sharing'),
    url(r'^sharing.html/?$', views.redirect_to_name, {'url_name':'sharing'}),

    # Global network pages

    url(r'^network/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/network.html'),
        name='network'),
    url(r'^international.html/?$', views.redirect_to_name, {'url_name':'network'}),

    url(r'^join-network/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/join-network.html'),
        name='join-network'),

    url(r'^organization',
        include('organization.urls', namespace="organization")),
    url(r'^harvard',
        include('harvard.urls', namespace="harvard")),
    url(r'^canada',
        include('canada.urls', namespace="canada")),
    url(r'^uk',
        include('uk.urls', namespace="uk")),

    # Support page

    url(r'^donate/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/donate.html'),
        name='donate'),
    url(r'donate.html/?$', views.redirect_to_name, {'url_name':'donate'}),
    url(r'donate/?$', views.redirect_to_name, {'url_name':'donate'}),
    url(r'donate/index.html/?$', views.redirect_to_name, {'url_name':'donate'}),
    url(r'donate/other.html/?$', views.redirect_to_name, {'url_name':'donate'}),
    url(r'donate/matching.html/?$', views.redirect_to_name, {'url_name':'donate'}),

    # Footer pages

    url(r'^contact-us/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/contact-us.html'),
        name='contact-us'),
    url(r'contact.html', views.redirect_to_name, {'url_name':'contact-us'}),
    url(r'^tos/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/tos.html'),
        name='tos'),
    url(r'tos.html', views.redirect_to_name, {'url_name':'tos'}),
    url(r'^website-privacy-policy/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/website-privacy-policy.html'),
        name='website-privacy-policy'),
    url(r'privacypolicy.html/?$', views.redirect_to_name, {'url_name':'website-privacy-policy'}),

    # Unlinked by existing pages
    url(r'getlabs2014/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/getlabs2014.html'),
        name='getlabs2014'),

    # Additional redirects

    url(r'^consent/?$', views.redirect_to_name, {'url_name':'harvard:documents'}),
    url(r'^consent/index.html/?$', views.redirect_to_name, {'url_name':'harvard:documents'}),
    url(r'^medicalcenters.html/?$', views.redirect_to_name, {'url_name':'harvard:collection-centers'}),
    url(r'^howitworks.html/?$', views.redirect_to_name, {'url_name':'harvard:howitworks'}),
    url(r'consent/PGP_Consent_Approved_02212013.pdf',
        RedirectView.as_view(url='/static/docs/harvard/PGP_Consent_Approved_02212013.pdf')),
    url(r'exam/v20120430-study-guide.pdf',
        RedirectView.as_view(url='/static/docs/harvard/v20120430-study-guide.pdf')),

)
