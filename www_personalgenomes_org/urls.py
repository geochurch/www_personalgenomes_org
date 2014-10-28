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
    url(r'^mission/?$', views.redirect_to_name, {'url_name': 'organization:mission'}),
    url(r'^mission.html/?$', views.redirect_to_name, {'url_name': 'organization:mission'}),
    url(r'^about.html/?$', views.redirect_to_name, {'url_name': 'organization:mission'}),

    url(r'^people/?$', views.redirect_to_name, {'url_name': 'organization:people'}),
    url(r'^people.html/?$', views.redirect_to_name, {'url_name': 'organization:people'}),

    url(r'^press/?', views.redirect_to_name, {'url_name': 'organization:press'}),
    url(r'^news.html/?$', views.redirect_to_name, {'url_name': 'organization:press'}),

    url(r'^publications/?', views.redirect_to_name, {'url_name': 'organization:publications'}),
    url(r'^research.html/?$', views.redirect_to_name, {'url_name': 'organization:publications'}),

    # Participate pages
    url(r'^pgp/?$', views.redirect_to_name, {'url_name': 'organization:pgp'}),
    url(r'^project.html/?$', views.redirect_to_name, {'url_name': 'organization:pgp'}),

    url(r'^why-participate/?', views.redirect_to_name, {'url_name': 'organization:why-participate'}),
    url(r'^whyparticipate.html/?$', views.redirect_to_name, {'url_name': 'organization:why-participate'}),

    url(r'^non-anonymous/?', views.redirect_to_name, {'url_name': 'organization:non-anonymous'}),

    url(r'^risks-benefits/?', views.redirect_to_name, {'url_name': 'organization:risks-benefits'}),
    url(r'^considerations.html/?$', views.redirect_to_name, {'url_name': 'organization:risks-benefits'}),

    url(r'^pgp-sign-up/?', views.redirect_to_name, {'url_name':'organization:pgp-sign-up'}),
    url(r'^signup.html/?$', views.redirect_to_name, {'url_name':'organization:pgp-sign-up'}),
    url(r'^eligibility.html/?$', views.redirect_to_name, {'url_name':'organization:pgp-sign-up'}),

    # Research pages
    url(r'^get-data/?$', views.redirect_to_name, {'url_name': 'organization:get-data'}),

    url(r'^sharing/?',views.redirect_to_name, {'url_name':'organization:sharing'}),
    url(r'^sharing.html/?$', views.redirect_to_name, {'url_name':'organization:sharing'}),

    # Global network pages
    url(r'^network/?$', views.redirect_to_name, {'url_name':'organization:network'}),
    url(r'^international.html/?$', views.redirect_to_name, {'url_name':'organization:network'}),

    url(r'^join-network/?$', views.redirect_to_name, {'url_name':'organization:join-network'}),

    url(r'^organization',
        include('organization.urls', namespace="organization")),
    url(r'^harvard',
        include('harvard.urls', namespace="harvard")),
    url(r'^canada',
        include('canada.urls', namespace="canada")),
    url(r'^uk',
        include('uk.urls', namespace="uk")),
    url(r'^austria',
        include('austria.urls', namespace="austria")),

    # Support page
    url(r'^donate/?$', views.redirect_to_name, {'url_name':'organization:donate'}),
    url(r'^donate.html/?$', views.redirect_to_name, {'url_name':'organization:donate'}),
    url(r'^donate/?$', views.redirect_to_name, {'url_name':'organization:donate'}),
    url(r'^donate/index.html/?$', views.redirect_to_name, {'url_name':'organization:donate'}),
    url(r'^donate/other.html/?$', views.redirect_to_name, {'url_name':'organization:donate'}),
    url(r'^donate/matching.html/?$', views.redirect_to_name, {'url_name':'organization:donate'}),

    # Internationalization language-handling views
    (r'^i18n/', include('django.conf.urls.i18n')),

    # Footer pages
    url(r'^tos/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/tos.html'),
        name='tos'),
    url(r'^tos.html', views.redirect_to_name, {'url_name':'tos'}),
    url(r'^website-privacy-policy/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/website-privacy-policy.html'),
        name='website-privacy-policy'),
    url(r'^privacypolicy.html/?$', views.redirect_to_name, {'url_name':'website-privacy-policy'}),

    # Unlinked by existing pages
    url(r'getlabs2014/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/getlabs2014.html'),
        name='getlabs2014'),

    # Additional redirects
    url(r'^contact-us/?$', views.redirect_to_name, {'url_name':'organization:contact-us'}),
    url(r'^contact.html', views.redirect_to_name, {'url_name':'organization:contact-us'}),
    url(r'^consent/?$', views.redirect_to_name, {'url_name':'harvard:documents'}),
    url(r'^consent/index.html/?$', views.redirect_to_name, {'url_name':'harvard:documents'}),
    url(r'^medicalcenters.html/?$', views.redirect_to_name, {'url_name':'harvard:collection-centers'}),
    url(r'^howitworks.html/?$', views.redirect_to_name, {'url_name':'harvard:howitworks'}),
    url(r'^consent/PGP_Consent_Approved_02212013.pdf',
        RedirectView.as_view(url='/static/docs/harvard/PGP_Consent_Approved_02212013.pdf')),
    url(r'^exam/v20120430-study-guide.pdf',
        RedirectView.as_view(url='/static/docs/harvard/v20120430-study-guide.pdf')),

)
