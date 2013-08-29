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
    url(r'^/historic-documents/?', TemplateView.as_view(template_name='harvard/historic-documents.html'),
        name='historic-documents'),
    url(r'^/protocols/?', TemplateView.as_view(template_name='harvard/protocols.html'),
        name='protocols'),
    url(r'^/collection-centers/?', TemplateView.as_view(template_name='harvrd/collection-centers.html'),
        name='collection-centers'),
    url(r'^/data/?', TemplateView.as_view(template_name='harvard/data.html'),
        name='data'),
    )
