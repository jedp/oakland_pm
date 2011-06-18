import settings
from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request):
    return render_to_response(
            'feed.html', 
            {},
            context_instance=RequestContext(request))
    
def feed(request):
    return render_to_response(
            'feed.html', 
            {},
            context_instance=RequestContext(request))

def event(request):
    return render_to_response(
            'event_detail.html', 
            {},
            context_instance=RequestContext(request))

def categories(request):
    return render_to_response(
            'categories.html', 
            {},
            context_instance=RequestContext(request))
