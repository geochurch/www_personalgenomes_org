from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='canada/index.html'),
        name='index'),
    url(r'^/project/?', TemplateView.as_view(template_name='canada/project.html'),
        name='project'),
    url(r'^/consent/?', TemplateView.as_view(template_name='canada/consent.html'),
        name='consent'),
    url(r'^/contact/?$', views.contact, name='contact'),
    )
