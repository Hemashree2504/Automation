import os
import platform

import pytest

from Functions.LaunchBrowser import LaunchBrowser
from Functions.Pages import Pages


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="", help="browser")
    parser.addoption("--url", action="store", default="", help="url")
    parser.addoption("--search", action="append", default=[], help="input search")


@pytest.fixture(scope='function')
def test_browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='function')
def test_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope='function')
def test_search(request):
    return request.config.getoption("--search")


@pytest.fixture(scope='function')
def browser(request, test_browser_name):
    browser_name = test_browser_name
    print(browser_name)
    lb = LaunchBrowser()
    request.node.driver = lb.launch_browser(browser_name)
    yield request.node.driver
    request.node.driver.quit()


@pytest.fixture(scope='function')
def test_case(
        browser,
        test_url,
        test_search

):
    class WebEnvironmentSetup(Pages):
        def __init__(self):
            self.driver = browser
            self.url = test_url
            self.search = test_search

    test_case_template_init = WebEnvironmentSetup()
    yield test_case_template_init
