from django.test import LiveServerTestCase
from selenium import webdriver


class T1Test(LiveServerTestCase):
	fixtures = ['initial_data.json']

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_t1(self):
		self.browser.get(self.live_server_url)
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Yaroslav', body.text)
		self.assertIn('sokolovsky.y', body.text)