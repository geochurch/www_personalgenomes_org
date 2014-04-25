from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='organization/index.html'),
        name='index'),

    # About pages

    url(r'^/mission/?$',
        TemplateView.as_view(template_name='organization/mission.html'),
        name='mission'),

    url(r'^/people/?$',
        TemplateView.as_view(template_name='organization/people.html'),
        name='people'),

    url(r'^/sharing/?',
        TemplateView.as_view(template_name='organization/sharing.html'),
        name='sharing'),

    url(r'^/data/?',
        TemplateView.as_view(template_name='organization/data.html'),
        name='get-data'),

    url(r'^/contact-us/?',
        TemplateView.as_view(template_name='organization/contact-us.html'),
        name='contact-us'),

    url(r'^/press/?',
        TemplateView.as_view(template_name='organization/press.html'),
        name='press'),

    url(r'^/publications/?',
        TemplateView.as_view(template_name='organization/publications.html'),
        name='publications'),

    # Participate pages

    url(r'^/pgp/?$',
        TemplateView.as_view(template_name='organization/pgp.html'),
        name='pgp'),

    url(r'^/why-participate/?',
        TemplateView.as_view(template_name='organization/why-participate.html'),
        name='why-participate'),

    url(r'^/non-anonymous/?',
        TemplateView.as_view(template_name='organization/non-anonymous.html'),
        name='non-anonymous'),

    url(r'^/risks-benefits/?',
        TemplateView.as_view(template_name='organization/risks-benefits.html'),
        name='risks-benefits'),

    url(r'^/pgp-sign-up/?',
        TemplateView.as_view(template_name='organization/pgp-sign-up.html'),
        name='pgp-sign-up'),

    # Global network pages

    url(r'^/network/?$',
        TemplateView.as_view(template_name='organization/network.html'),
        name='network'),

    url(r'^/join-network/?$',
        TemplateView.as_view(template_name='organization/join-network.html'),
        name='join-network'),

    # Support page

    url(r'^/donate/?$',
        TemplateView.as_view(template_name='organization/donate.html'),
        name='donate'),
    )
