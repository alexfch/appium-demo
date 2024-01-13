import os

import pytest
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


@pytest.mark.skip("TBD")
def test_ios_simulate_network_conditions():
    pass


@pytest.mark.skip("TBD")
def test_ios_simulate_gps():
    pass


@pytest.mark.skip("TBD")
def test_ios_multi_action():
    pass


@pytest.mark.skip("TBD")
def test_ios_touch_action():
    pass


@pytest.mark.skip("TBD")
def test_ios_action_helpers():
    pass


@pytest.mark.skip("TBD")
def test_ios_context():
    pass


@pytest.mark.skip("TBD")
def test_ios_device():
    pass


@pytest.mark.skip("TBD")
def test_ios_execute_mobile_command():
    pass


@pytest.mark.skip("TBD")
def test_ios_hw_actions():
    pass


@pytest.mark.skip("TBD")
def test_ios_image_comparison():
    pass


@pytest.mark.skip("TBD")
def test_ios_keyboard():
    pass


@pytest.mark.skip("TBD")
def test_ios_location():
    pass


@pytest.mark.skip("TBD")
def test_ios_log_event():
    pass


@pytest.mark.skip("TBD")
def test_ios_remote_fs():
    pass


@pytest.mark.skip("TBD")
def test_ios_screen_record():
    pass


@pytest.mark.skip("TBD")
def test_ios_settings():
    pass


@pytest.mark.skip("TBD")
def test_appium_service():
    pass


@pytest.mark.skip("TBD")
def test_ios_application_state():
    pass

