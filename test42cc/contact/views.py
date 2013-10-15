from django.shortcuts import render_to_response
from django.template import RequestContext
from test42cc.contact.models import Contact


def index(request):
    contact = Contact.objects.get(pk=1)
    return render_to_response(
        'contact.html', {'contact': contact},
        context_instance=RequestContext(request))