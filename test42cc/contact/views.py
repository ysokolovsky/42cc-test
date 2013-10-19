from django.shortcuts import render_to_response
from django.template import RequestContext
from test42cc.contact.models import Contact, Request
from test42cc.contact.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import json
from django.http import HttpResponse


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


def to_json(response, **kwargs):
    response = HttpResponse(json.dumps(response))
    response['mimetype'] = "text/javascript"
    response['Pragma'] = "no cache"
    response['Cache-Control'] = "no-cache, must-revalidate"
    return response

@login_required()
def edit_contacts_ajax(request):
    contact = Contact.objects.get(pk=1)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return to_json({'status': 'success', 'data': str(reverse('edit_contacts'))})
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
            return HttpResponse(json.dumps({'response': response, 'result': 'error'}))

    return to_json({'status': 'error', 'data': None})


@login_required()
def edit_contacts(request):
    contact = Contact.objects.get(pk=1)
    form = ContactForm(instance=contact)

    return render_to_response(
        'contact/edit.html', {'form': form},
        context_instance=RequestContext(request))
