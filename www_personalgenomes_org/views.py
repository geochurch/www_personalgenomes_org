from django.contrib.gis.geoip import GeoIP
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.http import is_safe_url


def csrf_failure(request, reason=""):
    response = "Request failed. Reason: " + reason
    if reason == 'CSRF cookie not set.':
        response += (
            "<h4>Do you have cookies disabled?</h4> " +
            "<p>Sorry, we're unable to complete this request because we " +
            "didn't receive an authentication cookie.</p>" +
            "<p>This may be because you have prevented the site from " +
            "using cookies. If this is true, many features (e.g. language " +
            "preferences) will be unavailable to you.</p>"
            "<p>If you do allow cookies and still see this message, this " +
            "may be a bug in the site. You can contact site administrators " +
            "at website@personalgenomes.org.</p>")
    next = request.META.get('HTTP_REFERER')
    if not is_safe_url(url=next, host=request.get_host()):
        next = '/'
    response += '<p><a href="' + next + '">Click here to return</a></p>'
    return HttpResponse(response)


def redirect_to_name(request, url_name):
    """Redirects to URL with name url_name"""
    return redirect(url_name)


def get_client_ip(request):
    ip = request.META.get('HTTP_X_REAL_IP')
    if not ip:
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if not ip:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    """Displays index with IP..."""
    ip = get_client_ip(request)
    # Use the below to test local behavior during development
    #ip = '128.40.250.113' # UK
    #ip = '134.174.150.3' # US
    #ip = '192.75.158.248' # CA
    g = GeoIP()
    country_code = g.country(ip)['country_code']
    if country_code == 'CA':
        return render(request, 'canada/index.html')
    elif country_code == 'GB':
        return render(request, 'uk/index.html')
    elif country_code == 'US':
        return render(request, 'harvard/index.html')
    elif country_code == 'AT':
        return render(request, 'austria/index.html')
    else:
        return render(request, 'www_personalgenomes_org/index.html')
