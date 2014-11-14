from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='austria/index.html'),
        name='index'),
    url(r'^/about/?', TemplateView.as_view(template_name='austria/about.html'),
        name='about'),
    url(r'^/team/?', TemplateView.as_view(template_name='austria/people.html'),
        name='people'),
    url(r'^/volunteer/?', TemplateView.as_view(template_name='austria/sign-up.html'),
        name='sign-up'),
    url(r'^/data/?', TemplateView.as_view(template_name='austria/data.html'),
        name='data'),
    url(r'^/news/?', TemplateView.as_view(template_name='austria/news.html'),
        name='news'),
    url(r'^/global-network/?', TemplateView.as_view(template_name='austria/global-network.html'),
        name='global-network'),
    url(r'^/contact-us/?', TemplateView.as_view(template_name='austria/contact-us.html'),
        name='contact-us'),
    url(r'^/project/?', TemplateView.as_view(template_name='austria/project.html'),
        name='project'),
    url(r'^/consent/?', TemplateView.as_view(template_name='austria/consent.html'),
        name='consent'),
    )
