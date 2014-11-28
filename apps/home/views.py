from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def home(request):
    context = {}
    return render_to_response('home/index.html', context, RequestContext(request))