from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import RedirectView
from django.shortcuts import redirect, render
from django.contrib.gis.geoip import GeoIP

def redirect_to_name(request, url_name):
    """Redirects to URL with name url_name"""
    return redirect(url_name)

def get_client_ip(request):
    ip = request.META.get('HTTP_X_REAL_IP')
    if not ip:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    """Displays index with IP..."""
    ip = get_client_ip(request)
    g = GeoIP()
    return render(request, 'www_personalgenomes_org/index.html', {'ip': ip, 'country': g.country(ip)})
