import os


def test_device_orientation(appium_service, ios_driver_factory):
    with ios_driver_factory({
        'appium:app': os.path.join(os.getenv('PROJECT_PATH'), 'app', 'my-test-ios-app.app')
    }) as driver:
        driver.orientation = "LANDSCAPE"
        assert driver.orientation == "LANDSCAPE"
        driver.orientation = "PORTRAIT"
        assert driver.orientation == "PORTRAIT"


