from django.forms import ModelForm
from test42cc.contact.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact