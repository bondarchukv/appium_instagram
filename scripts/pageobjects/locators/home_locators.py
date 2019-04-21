from appium.webdriver.common.mobileby import MobileBy

class HomePageLocators(object):
    SECURITY_TEXT = (MobileBy.XPATH, "//h2[text() = 'We Detected An Unusual Login Attempt']")
    ADDINSTA_TEXT = (MobileBy.XPATH, "//h2[text() = 'Add Instagram to your Home screen?']")