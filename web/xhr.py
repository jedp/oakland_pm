import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def get_csrf(request):
    c = {}
    c.update(csrf(request))    
    return c

def feed(request):
    """Return a list of events"""
    c = get_csrf(request)    
    return render_to_response(
            'list_events.html', 
            {"c":c,
             "events": ['foo']},
            context_instance=RequestContext(request))

def event(request, event_id):
    c = get_csrf(request)    
    return render_to_response(
            'event_detail.html', 
            {"c":c},
            context_instance=RequestContext(request))

def categories(request):
    c = get_csrf(request)    
    return render_to_response(
            'list_events.html', 
            {"c":c},
            context_instance=RequestContext(request))


