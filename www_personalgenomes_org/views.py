from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import RedirectView

class ReverseRedirectView(RedirectView):

    def get_redirect_url(self):
        return reverse_lazy(self.url, args=[u""])
