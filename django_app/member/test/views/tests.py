from django.test import TestCase
from django.urls import reverse, resolve
from .. import views


class LoginViewTest(TestCase):
    VIEW_URL = '/member/login'
    VIEW_URL_NAME = 'member:login'
    

    def test_url_equal_reverse_url_name(self):
        self.assertEqual(self.VIEW_URL, reverse(self.VIEW_URL_NAME))

    def test_url_resolves_to_login_view(self):
        # login view가 특정 url을 사용하고 있는지
        # resolve함수를 이용해 특정 URL이 참조하는 view검색
        found = resolve(self.VIEW_URL)
        # print(found)
        # print(found.func)
        # print(views.login)


        # 특정 view에 해당하는 함수 (.func속성)과 views.login함수가 같은지 확인
        self.assertEqual(found.func, views.login)


    def test_uses_login_template(self):
        # login view가 member/login.html을 사용하고 있는지
        url = reverse(self.VIEW_URL)
        response = self.client.get(url)
        self.assertTemplateUsed(response, self.VIEW_URL_NAME)

