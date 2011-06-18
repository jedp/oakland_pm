import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def home(request):
    return render_to_response('home.html', 
            context_instance=RequestContext(request))
    
def feed(request):
    return render_to_response('feed.html', 
            {'events': ['foo']},
            context_instance=RequestContext(request))

def search(request):
    return render_to_response('search.html',
            context_instance=RequestContext(request))

def friends(request):
    return render_to_response('friends.html',
            context_instance=RequestContext(request))

def messages(request):
    return render_to_response('messages.html',
            context_instance=RequestContext(request))

def event(request, event_id):
    return render_to_response('event.html', 
            context_instance=RequestContext(request))

def categories(request):
    return render_to_response('categories.html', 
            context_instance=RequestContext(request))

def get_csrf(request):
    c = {}
    c.update(csrf(request))    
    return c
