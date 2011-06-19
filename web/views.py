import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.core.context_processors import csrf

from core.models import *

def get_csrf(request):
    c = {}
    c.update(csrf(request))    
    return c

def home(request):
    return render_to_response('home.html', 
            {'c': get_csrf(request)},
            context_instance=RequestContext(request))
    
def feed(request):
    return render_to_response('feed.html', 
            {'events': ['foo'],
             'c': get_csrf(request)},
            context_instance=RequestContext(request))

def search(request):
    return render_to_response('search.html',
            {'c': get_csrf(request)},
            context_instance=RequestContext(request))

def friends(request):
    return render_to_response('friends.html',
            {'c': get_csrf(request)},
            context_instance=RequestContext(request))

def messages(request):
    return render_to_response('messages.html',
            {'c': get_csrf(request)},
            context_instance=RequestContext(request))

def event(request, event_id):
    program = Program.objects.get(id=event_id)
    #eventData = render_to_string('my_template.html', { 'foo': 'bar' })
    return render_to_response('event.html', 
            {'c': get_csrf(request), "program":program},
            context_instance=RequestContext(request))

def category(request, name):
    """
    Get selected category and all projects and their tags
    """
    selected = Category.objects.get(name=name)
    programs = Program.objects.filter(categories=selected)
    tags = Tag.objects.filter(program__categories=selected)
    return render_to_response('categories.html', 
            {'c': get_csrf(request),
             'categories': Category.objects.all(),
             'programs': programs,
             'selected': selected,
             'tags': tags},
            context_instance=RequestContext(request))

def categories(request):
    return render_to_response('categories.html', 
            {'c': get_csrf(request),
             'categories': Category.objects.all()},
            context_instance=RequestContext(request))
    
def about(request):
    return render_to_response('about.html', 
            {'c': get_csrf(request)},
            context_instance=RequestContext(request))
