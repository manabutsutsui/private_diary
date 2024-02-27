from django.test import LiveServerTestCase
from django.urls import reverse_lasy
from selenium.webdriver.chrome.webdriver import WebDriver

# Create your tests here.
class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='C:\Program Files (x86)\WebDriver\chromedriver.exe')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

        username_input = self.selenium.find_element_by_name('login')
        username_input.send_keys('tsutsuimanabu16@gmail.com')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('testpassword')
        self.selenium.find_element_by_class_name('btn').click()

        self.assertEquals('日記一覧 | Private Diary', self.selenium.title)