from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='harvard/index.html'),
        name='index'),
    url(r'^/people/?', TemplateView.as_view(template_name='harvard/people.html'),
        name='people'),
    url(r'^/documents/?', TemplateView.as_view(template_name='harvard/documents.html'),
        name='documents'),
    )
