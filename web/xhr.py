import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def home(request):
    c = get_csrf(request)    
    return render_to_response(
            'base.html', 
            {"c":c},
            context_instance=RequestContext(request))
    
def feed(request):
    c = get_csrf(request)    
    return render_to_response(
            'feed.html', 
            {"c":c},
            context_instance=RequestContext(request))

def event(request):
    c = get_csrf(request)    
    return render_to_response(
            'event_detail.html', 
            {"c":c},
            context_instance=RequestContext(request))

def categories(request):
    c = get_csrf(request)    
    return render_to_response(
            'categories.html', 
            {"c":c},
            context_instance=RequestContext(request))

def base(request):
    c = get_csrf(request)
    return render_to_response(
            'base.html', 
            {"c":c},
            context_instance=RequestContext(request))


def get_csrf(request):
    c = {}
    c.update(csrf(request))    
    return c