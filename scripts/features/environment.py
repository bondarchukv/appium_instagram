import os
from appium import webdriver

def before_feature(context,feature):
        context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'browserName':'Chrome',
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'Nexus_5X_API_28',
            'fastReset': True
        })
        context.driver.implicitly_wait(5)


def after_feature(context,feature):
        context.driver.quit()