from django.conf.urls import patterns, url
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='uk/index.html'),
        name='index'),
    url(r'^/about-pgp/?', TemplateView.as_view(template_name='uk/about-pgp.html'),
        name='about-pgp'),
    url(r'^/about-us/?', TemplateView.as_view(template_name='uk/about-us.html'),
        name='about-us'),
    url(r'^/sign-up/?', TemplateView.as_view(template_name='uk/sign-up.html'),
        name='sign-up'),
    url(r'^/data/?', TemplateView.as_view(template_name='uk/data.html'),
        name='data'),
    url(r'^/news/?', TemplateView.as_view(template_name='uk/news.html'),
        name='news'),
    )
