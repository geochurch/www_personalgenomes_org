from django.conf.urls import patterns, url
from django.views.generic import RedirectView, TemplateView
from www_personalgenomes_org.views import redirect_to_name

urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='harvard/index.html'),
        name='index'),
    url(r'^/about-us/?', TemplateView.as_view(template_name='harvard/about-us.html'),
        name='about-us'),
    url(r'^/about-pgp/?', TemplateView.as_view(template_name='harvard/about-pgp.html'),
        name='about-pgp'),
    url(r'^/sign-up/?', TemplateView.as_view(template_name='harvard/sign-up.html'),
        name='sign-up'),
    url(r'^/news/?', TemplateView.as_view(template_name='harvard/news.html'),
        name='news'),


    url(r'^/historic-documents/?', TemplateView.as_view(template_name='harvard/historic-documents.html'),
        name='historic-documents'),
    url(r'^/howitworks/?', TemplateView.as_view(template_name='harvard/howitworks.html'),
        name='howitworks'),
    url(r'^/collection-centers/?', TemplateView.as_view(template_name='harvard/collection-centers.html'),
        name='collection-centers'),
    url(r'^/data/?', TemplateView.as_view(template_name='harvard/data.html'),
        name='data'),

    url(r'^/documents/?', RedirectView.as_view(url='/harvard/sign-up#documents'),
        name='documents'),

    url(r'^/people/?$', redirect_to_name, {'url_name': 'harvard:about-us'}),
    url(r'^/protocols/?', redirect_to_name, {'url_name': 'harvard:sign-up'}),
    )
