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
