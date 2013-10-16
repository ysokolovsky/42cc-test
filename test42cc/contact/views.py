from django.shortcuts import render_to_response
from django.template import RequestContext
from test42cc.contact.models import Contact, Request


def index(request):
    contact = Contact.objects.get(pk=1)
    return render_to_response(
        'contact/contact.html', {'contact': contact},
        context_instance=RequestContext(request))


def show_requests(request):
    requests = Request.objects.all().order_by('time')[:10]
    return render_to_response(
        'contact/requests.html', {'requests': requests},
        context_instance=RequestContext(request))