import pytest


def test_android(appium_service, android_driver_factory):
    with android_driver_factory({
            'appium:app': '/path/to/app/test-app.apk',
            'appium:udid': '567890'
    }) as driver:
        el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'item')
        el.click()


@pytest.mark.skip("TBD")
def test_android_clipboard():
    pass

