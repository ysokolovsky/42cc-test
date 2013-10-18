from django.forms import ModelForm
from test42cc.contact.models import Contact
from test42cc.contact.widgets import DatepickerWidget


class ContactForm(ModelForm):
    class Meta:
        model = Contact

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['bday'].widget = DatepickerWidget(params="dateFormat: 'yy-mm-dd'")
        for myField in self.fields:
            if myField != 'photo':
                self.fields[myField].widget.attrs['class'] = 'form-control'

        contact = Contact.objects.get(pk=1)
        names = Contact._meta.get_all_field_names()

        for f in names:
            if f == 'id':
                continue
            self.fields[f].initial = getattr(contact, f)
        self.fields['photo'].initial = contact.photo
