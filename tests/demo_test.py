import os

from appium.webdriver.common.appiumby import AppiumBy


def test_ios(appium_service, ios_driver_factory):
    with ios_driver_factory({
        'appium:app': os.path.join(os.getenv('PROJECT_PATH'), 'app', 'my-test-ios-app.app')
    }) as driver:
        el = driver.find_element(by=AppiumBy.NAME, value='helloWorldText')
        assert el.text == "Hello, world!"
        btn = driver.find_element(by=AppiumBy.NAME, value='clickMeButton')
        btn.click()
        msg = driver.find_element(AppiumBy.NAME, "message")
        assert msg.text == "Yes! It's clicked!"


def test_android(appium_service, android_driver_factory):
    with android_driver_factory({
            'appium:app': '/path/to/app/test-app.apk',
            'appium:udid': '567890'
    }) as driver:
        el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'item')
        el.click()
