from django_webtest import WebTest
from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.template import RequestContext


class TestContact(WebTest):
    fixtures = ['initial_data.json']

    def test_t1_base(self):
        page = self.app.get(reverse('test42cc.contact.views.index'))
        assert u"Name" in page
        assert u"Last name" in page
        assert u"Yaroslav" in page
        assert u"Bio" in page
        assert u"Date of birth" in page
        assert u"1990" in page