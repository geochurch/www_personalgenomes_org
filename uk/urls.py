from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='uk/index.html'),
        name='index'),
    url(r'^/people/?', TemplateView.as_view(template_name='uk/people.html'),
        name='people'),
    url(r'^/enrollment/?', TemplateView.as_view(template_name='uk/enrollment.html'),
        name='enrollment'),
    url(r'^/documents/?', TemplateView.as_view(template_name='uk/documents.html'),
        name='documents'),
    )
