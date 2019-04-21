from appium.webdriver.common.mobileby import MobileBy

class LoginPageLocators(object):
    USERNAME = (MobileBy.NAME, 'username')
    PASSWORD = (MobileBy.NAME, 'password')
    LOGIN_BTN = (MobileBy.XPATH, "//button[@type='submit']/div")