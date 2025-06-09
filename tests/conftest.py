import os
import allure
import yaml
import pytest
from utils.config_loader import load_config
from utils.driver_factory import DriverFactory



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run in headless mode")

@pytest.fixture(scope='function')
def driver_setup(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = DriverFactory.get_driver(browser_name=browser, headless=headless)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs['driver_setup']
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG
        )


@pytest.fixture(scope="session")
def config():
    return load_config()


@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]


@pytest.fixture(scope="session")
def data_test():
    # Load the data from the YAML file
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, '..', 'config', 'data_test.yaml')
    config_path = os.path.abspath(config_path)
    with open(config_path, "r") as file:
        return yaml.safe_load(file)
