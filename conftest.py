import os

import pytest

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService


APPIUM_HOST = '127.0.0.1'
APPIUM_PORT = 4723


@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        args=['--address', APPIUM_HOST, '--port', str(APPIUM_PORT)],
        timeout_ms=20000
    )
    yield service
    service.stop()


def create_ios_driver(custom_opts=None):
    options = XCUITestOptions()
    options.platform_version = '17.1'
    options.udid = 'F0845E72-3EB4-4421-9DC0-3C703E71F18A'  # WHAT IS THE ID? WHAT TO TYPE HERE?
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


def create_android_driver(custom_opts=None):
    options = UiAutomator2Options()
    options.platform_version = '10'
    options.udid = '123456789ABC'
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


@pytest.fixture
def ios_driver_factory():
    return create_ios_driver


@pytest.fixture
def ios_driver():
    driver = create_ios_driver()
    yield driver
    driver.close()


@pytest.fixture
def android_driver_factory():
    return create_android_driver


@pytest.fixture
def android_driver():
    driver = create_android_driver()
    yield driver
    driver.close()


@pytest.fixture(autouse=True)
def before_and_after_test(request):
    os.environ["PROJECT_PATH"] = str(request.config.rootpath)
    yield
