# appium_instagram
Appium_instagram is a sample project that utilizes Python's BDD Behave framework along with Appium\ChromeDriver and Android Emulator to test a simple login into Instagram

## Installation
You need to have these installed in order to run the application:
* Python 2.7 or higher with PIP installed
* Behave for Python 
`pip install behave`
* Appium Client for Python
`pip install Appium-Python-Client`
* Android Emulator (Android Studio with Emulator and SDK will be the easiest way to run it)
* Appium (The Appium's desktop version is recommended as it simplifies the configuration a lot)
* ChromeDriver for Appium (please make sure to use [a proper chromedriver version](http://appium.io/docs/en/writing-running-appium/web/chromedriver/) )

## Configuration
Please edit `scripts\features\environment.py` file with your desired capabilities for Appium.
Also please set proper Instagram account settings inside `scripts\features\login.feature`.

## Run
Just execute behave inside the `scripts` folder.

## Test Results
Successful test results should look something like this:
```PS C:\Python27\Scripts> .\behave.exe
Feature: Instragram Login # features/login.feature:1
  In order to test the Instagram web application
  As a mobile user
  I want to be able to login into the application
  using already existing login credentials
  Scenario: Login                                                              # features/login.feature:7
    Given I open login page "https://www.instagram.com/accounts/login/"        # features/steps/steps.py:8
    When I login with email "YOUR_EMAIL" and password "YOUR_PASSWORD"          # features/steps/steps.py:14
    Then I am on main page                                                     # features/steps/steps.py:20

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m45.994s
```

## Notes
* For this simple test seeing a Security Check or Instagram Home Screen window is treated as a successful login.
* Environment & scenario configurations, logging, reporting and other useful stuff is out of the scope for this simple application :wink:

## License
[MIT](https://choosealicense.com/licenses/mit/)
