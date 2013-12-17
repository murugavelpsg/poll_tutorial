# Create your views here.
from django.http import HttpResponse, Http404
from polls.models import Poll
from django.template import Context, loader
from django.shortcuts import render_to_response

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index")
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)
    return HttpResponse(t.render(c))

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except:
        raise Http404
    return render_to_response('polls/detail.html', {'poll':p})

def results(request, poll_id):
    return HttpResponse("You're looking at results of poll %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s" % poll_id)

