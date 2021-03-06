from django.conf.urls import patterns, url
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='uk/index.html'),
        name='index'),
    url(r'^/about/?', TemplateView.as_view(template_name='uk/about.html'),
        name='about'),
    url(r'^/people/?', TemplateView.as_view(template_name='uk/people.html'),
        name='people'),
    url(r'^/sign-up/?', TemplateView.as_view(template_name='uk/sign-up.html'),
        name='sign-up'),
    url(r'^/data/?', TemplateView.as_view(template_name='uk/data.html'),
        name='data'),
    url(r'^/news-archive/?', TemplateView.as_view(template_name='uk/news-archive.html'),
        name='news-archive'),
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
