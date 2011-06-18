import settings
from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request):
    return render_to_response(
            'feed.html', 
            {},
            context_instance=RequestContext(request))


def debug(request):
    print request
    return render_to_response(
            'debug.html', 
            {'request':str(request)})

