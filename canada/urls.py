from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='canada/index.html'),
        name='index'),
    url(r'^/about-us/?', TemplateView.as_view(template_name='canada/about-us.html'),
        name='about-us'),
    url(r'^/about-pgp/?', TemplateView.as_view(template_name='canada/about-pgp.html'),
        name='about-pgp'),
    url(r'^/sign-up/?', TemplateView.as_view(template_name='canada/sign-up.html'),
        name='sign-up'),
    url(r'^/data/?', TemplateView.as_view(template_name='canada/data.html'),
        name='data'),
    url(r'^/news/?', TemplateView.as_view(template_name='canada/news.html'),
        name='news'),
    url(r'^/global-network/?', TemplateView.as_view(template_name='canada/global-network.html'),
        name='global-network'),

    url(r'^/project/?', TemplateView.as_view(template_name='canada/project.html'),
        name='project'),
    url(r'^/consent/?', TemplateView.as_view(template_name='canada/consent.html'),
        name='consent'),
    url(r'^/contact/?$', views.contact, name='contact'),
    )
