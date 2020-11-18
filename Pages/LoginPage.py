from selenium.webdriver.common.by import By

from Git.Config.config import TestData
from Git.Pages.BasePage import Base


class Login(Base):
    # By locators
    Email = (By.ID, "username")
    Password = (By.ID, "password")
    Login_button = (By.ID, "loginBtn")
    SignUp_link = (By.LINK_TEXT, "Sign up")
    # Construcor of the page class

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(TestData.Base_url)
    # Page Action for login Page

    # this is used to get the page title

    def get_login_page_title(self, title):
       return self.get_title(title)

    # this is used to check sign up link

    def is_signup_link_exist(self):
        return self.is_visible(self.SignUp_link)

    # this is used to login to app

    def do_login(self, username, password):
        self.do_send_keys(self.Email, username)
        self.do_send_keys(self.Password, password)
        self.do_click(self.Login_button)

