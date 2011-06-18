import settings
from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request):
    print settings.STATIC_URL
    return render_to_response(
            'feed.html', 
            {},
            context_instance=RequestContext(request))


