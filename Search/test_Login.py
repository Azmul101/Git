import pytest

from Git.Config.config import TestData
from Git.Pages.LoginPage import Login
from Git.Search.Configtest import BaseTest


class TestLogin(BaseTest):

    def test_signup_link_visible(self):
        self.Login = Login(self.driver)
        flag = self.Login.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.Login = Login(self.driver)
        title = self.Login.get_title(TestData.Login_page_title)
        assert title == TestData.Login_page_title

    def test_login(self):
        self.Login = Login(self.driver)
        self.Login.do_login(TestData.User_name, TestData.Password)



