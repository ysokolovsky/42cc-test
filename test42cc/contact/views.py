from django.shortcuts import render_to_response
from django.template import RequestContext
from test42cc.contact.models import Contact, Request
from test42cc.contact.forms import ContactForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


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


@login_required()
def edit_contacts(request):
    contact = Contact.objects.get(pk=1)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/')   
    else:
        form = ContactForm() # An unbound form

    return render_to_response(
        'contact/edit.html', {'contact': contact, 'form': form},
        context_instance=RequestContext(request))
