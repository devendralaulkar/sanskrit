# Create your views here.
from django.template import RequestContext, Context, loader
from django.conf import settings
from django.shortcuts import render_to_response

def default(request):

    return render_to_response('shivsutra/index.html',
                              {},
                              context_instance=RequestContext(request))

def learn(request):

    return render_to_response('shivsutra/learn.html',
                              {},
                              context_instance=RequestContext(request))

def js(request):

    return render_to_response('shivsutra/js1.html',
                              {},
                              context_instance=RequestContext(request))
