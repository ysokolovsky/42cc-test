import json
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from test42cc.contact.models import Contact, Request
from test42cc.contact.forms import ContactForm, PriorityForm


def index(request):
    contact = Contact.objects.get(pk=1)
    return render_to_response(
        'contact/contact.html', {'contact': contact},
        context_instance=RequestContext(request))


def show_requests(request):
    requests = Request.objects.all().order_by('priority')[:10]

    if request.method == 'POST':
        form = PriorityForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['priority'] == 1:
                requests = Request.objects.all().order_by('-priority')[:10]
    else:
        form = PriorityForm()

    return render_to_response(
        'contact/requests.html', {'requests': requests, 'form': form},
        context_instance=RequestContext(request))


@login_required()
def edit_contacts(request):
    contact = Contact.objects.get(pk=1)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return HttpResponse(json.dumps({'status': 'success', 'data': str(reverse('edit_contacts'))}))
            else:
                return redirect(reverse('index'))
        else:
            if request.is_ajax():
                response = {}
                for k in form.errors:
                    response[k] = form.errors[k][0]
                return HttpResponse(json.dumps({'response': response, 'result': 'error'}))
    else:
            form = ContactForm()

    return render_to_response(
        'contact/edit.html', {'form': form},
        context_instance=RequestContext(request))
