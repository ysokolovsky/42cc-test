from django_webtest import WebTest
from StringIO import StringIO
from django.http import HttpRequest
from django.template import RequestContext, Template, Context
from django.contrib.auth import authenticate
from django.core.management import get_commands, call_command
from django.core.urlresolvers import reverse
from test42cc.contact.models import Request, Contact, Signals
from test42cc.contact.forms import ContactForm


class TestContact(WebTest):
    fixtures = ['initial_data.json']

    def test_t1_base(self):
        page = self.app.get(reverse('index'))
        assert u"Name" in page
        assert u"Last name" in page
        assert u"Yaroslav" in page
        assert u"Bio" in page
        assert u"Date of birth" in page
        assert u"1990" in page

    def test_t3_midreq(self):
        page = self.app.get(reverse('show_requests'))
        self.assertEqual(page.status, '200 OK')
        req = Request.objects.get(pk=1)
        assert reverse('show_requests') in req.path
        assert 'GET' in req.method
        for x in xrange(0,10):
            page = self.app.get(reverse('show_requests'))
        count = Request.objects.count()
        self.assertEqual(count, 11)
        page = self.app.get(reverse('show_requests'))
        self.assertEqual(str(page).count("Time:"), 10)

    def test_t4_contx_proc(self):
        context = RequestContext(HttpRequest())
        self.assertTrue('settings' in context)

    def test_t5_edit(self):
        #test login and data save
        page = self.client.get(reverse('edit_contacts'))
        self.assertRedirects(page, reverse('login')+'?next=/edit/')
        self.client.login(username='admin', password='admin')
        page = self.client.get(reverse('edit_contacts'))
        self.assertEqual(page.status_code, 200)
        data = {
            'f_name': "foo",
            'l_name': "bar",
            'bday': '2000-12-12',
            'bio': 'bio',
            'email': 'ya@yandex.ru',
            'jabber': 'ya@jabber.org',
            'skype': 'skype1',
            'other': 'other2'
        }
        page = self.client.post(reverse('edit_contacts'), data)
        page = self.app.get(reverse('index'))
        assert u"foo" in page
        assert u"bar" in page
        assert u"2000-12-12" in page
        assert u"bio" in page
        assert u"ya@yandex.ru" in page
        assert u"ya@jabber.org" in page
        assert u"skype1" in page
        assert u"other2" in page

    def test_t5_negative_data(self):
        #test on negative data
        data = {
            'f_name': "foo",
            'l_name': "",
            'bday': '1990-01-bh',
            'bio': 'bio',
            'email': 'ya@yandex.ru',
            'jabber': 'ya@jabber.org',
            'skype': 'skype1',
            'other': 'other2'
        }
        form = ContactForm(data=data)
        assert u'This field is required' in str(form)
        assert u'valid date' in str(form)

    def test_t6_ajax(self):
        self.client.login(username="admin", password="admin")
        data = {
            'f_name': "foo",
            'l_name': "bar",
            'bday': '2000-12-12',
            'bio': 'bio',
            'email': 'ya@yandex.ru',
            'jabber': 'ya@jabber.org',
            'skype': 'skype1',
            'other': 'other2'
        }
        page = self.client.post(reverse('edit_contacts'), data,
                                    follow=True,
                                    **{'HTTP_X_REQUESTED_WITH':
                                        'XMLHttpRequest'})
        self.assertContains(page, 'success')

    def test_t6_widget(self):
        widget_static = [
            'jquery-ui-1.10.3.custom.min.js',
            'main.js',
            'jquery-ui-1.10.3.custom.min.css'
        ]
        self.client.login(username='admin', password='admin')
        page = self.client.get(reverse('edit_contacts'))
        self.assertContains(page, 'id_bday')
        self.assertContains(page, 'datepicker')
        for script in widget_static:
            self.assertContains(page, script)

    def test_t8_tag(self):
        user = authenticate(username='admin', password='admin')
        tag = Template('{% load edittag %}{% edit_link user %}').render(Context({'user': user}))
        self.assertEqual('<a href="/admin/auth/user/1/">(admin)</a>', tag)
        self.client.login(username="admin", password="admin")
        page = self.client.get(reverse('index'))
        self.assertContains(page, '<a href="/admin/auth/user/1/">(admin)</a>')

    def test_t9_command(self):
        self.assertTrue('mycommand' in get_commands())
        content = StringIO()
        error = StringIO()
        call_command('mycommand', stdout=content, stderr=error, error=True)
        content.seek(0)
        error.seek(0)
        self.assertIn('Model:', content.read())
        self.assertIn('error:', error.read())
        assert u'models.Contact' in content.getvalue()
        assert u'Objects count: 1' in content.getvalue()
        assert u'models.Request' in content.getvalue()
        assert u'Objects count: 0' in content.getvalue()

    def test_t10_signals(self):
        Contact.objects.create(bday='1990-01-01')
        info = Contact.objects.latest('id')
        info.f_name = 'test'
        info.save()
        info.delete()
        signals = Signals.objects.order_by("-date")[:3]
        signals = list(signals)
        models_singals = [
            ['Contact', 'delete'],
            ['Contact', 'edit'],
            ['Contact', 'create'],
        ]
        self.assertEqual(len(signals), 3)
        for index, value in enumerate(models_singals):
            model, signal = value
            self.assertEqual(signals[index].model, model)
            self.assertEqual(signals[index].signal, signal)

    def test_t13_priority(self):
        page = self.client.post(reverse('show_requests'), {'priority': 1}, follow=True)
        self.assertIn('priority: 1', page)
