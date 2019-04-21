import time
from behave import *

from ... pageobjects.login import LoginPage
from ... pageobjects.home import HomePage


@given('I open login page "{url}"')
def step_impl(context, url):
   context.loginPage = LoginPage(context.driver)
   context.loginPage.goto_login_page(url)


@when('I login with email "{email}" and password "{password}"')
def step_impl(context, email, password):
   context.loginPage.enter_login_credentials(email, password)

#Please note that for Instagram`s sucessful login we will check landing on 
#Security Check or Add Instagram to Home Screen windows.
@then("I am on main page")
def step_impl(context):
    homePage = HomePage(context.driver)
    assert homePage.validate_login()