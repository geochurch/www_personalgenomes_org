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
    url(r'^/global-network/?', TemplateView.as_view(template_name='uk/global-network.html'),
        name='global-network'),
    url(r'^/contact-us/?', TemplateView.as_view(template_name='uk/contact-us.html'),
        name='contact-us'),
    url(r'^/email-storm-incident-and-apology-message/?', TemplateView.as_view(template_name='uk/email-storm-incident-and-apology-message.html'),
        name='email-storm-incident-and-apology-message'),
    url(r'^/email-storm-incident-and-apology/?', TemplateView.as_view(template_name='uk/email-storm-incident-and-apology.html'),
        name='email-storm-incident-and-apology'),
    )
