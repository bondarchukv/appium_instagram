from time import sleep
from base import Page
from locators.login_locators import *

class LoginPage(Page):

    def __init__(self, driver):
        Page.__init__(
            self,
            driver)

    def goto_login_page(self, url):
        self.open(url)

    def enter_username(self, username):
        u = self.find_element(LoginPageLocators.USERNAME)
        u.send_keys(username)

    def enter_password(self, password):
        ps = self.find_element(LoginPageLocators.PASSWORD)
        ps.send_keys(password)

    def click_login(self):
        b = self.find_element(LoginPageLocators.LOGIN_BTN)
        b.click()

    def enter_login_credentials(self, username, password):
            self.enter_username(username)
            self.enter_password(password)
            
            sleep(2)#wait for clear action (not ideal, but helps to skip retrying click_login method)            
            self.click_login()
