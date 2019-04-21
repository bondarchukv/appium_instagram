from base import Page
from locators.home_locators import *

class HomePage(Page):

    def __init__(self, context):
        Page.__init__(
            self,
            context)

    def validate_login(self):
        sec_found = self.wait_for_element(HomePageLocators.SECURITY_TEXT)
        print "sec_found %s" % sec_found
        add_found = self.wait_for_element(HomePageLocators.ADDINSTA_TEXT)
        print "add_found %s" % add_found
        return sec_found or add_found