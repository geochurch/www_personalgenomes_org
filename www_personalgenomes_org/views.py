from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import RedirectView
from django.shortcuts import redirect

class ReverseRedirectView(RedirectView):

    def get_redirect_url(self):
        return reverse_lazy(self.url, args=[u""])


def redirect_to_name(request, url_name):
    """Redirects to URL with name url_name"""
    return redirect(url_name)
