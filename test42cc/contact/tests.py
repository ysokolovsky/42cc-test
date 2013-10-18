from django_webtest import WebTest
from django.core.urlresolvers import reverse
from test42cc.contact.models import Request
from django.http import HttpRequest
from django.template import RequestContext


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
        page = self.app.get(reverse('edit_contacts'))
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
        self.assertRedirects(page, reverse('index'))
        page = self.app.get(reverse('index'))
        assert u"foo" in page
        assert u"bar" in page
        assert u"2000-12-12" in page
        assert u"bio" in page
        assert u"ya@yandex.ru" in page
        assert u"ya@jabber.org" in page
        assert u"skype1" in page
        assert u"other2" in page
        data = {
            'f_name': "foo",
            'l_name': "",
            'bday': 'ghggjjhg',
            'bio': 'bio',
            'email': 'ya@yandex.ru',
            'jabber': 'ya@jabber.org',
            'skype': 'skype1',
            'other': 'other2'
        }
        page = self.client.post(reverse('edit_contacts'), data)
        self.assertContains(page, 'This field is required')
        self.assertContains(page, 'valid date')

