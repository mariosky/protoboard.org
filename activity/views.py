# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    #Falta filtrar
    return render_to_response('activity/video_activity.html', {'name': 'Mario'}, context_instance=RequestContext(request))
