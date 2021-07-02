import pytest
from selenium import webdriver
import time
import os
from datetime import datetime

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



@pytest.fixture()
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge(
            executable_path="C:\\Users\\deepa\\AppData\\Local\\Programs\\Python\\Python39\\msedgedriver.exe")
    driver.implicitly_wait(5)
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def setup1(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge(
            executable_path="C:\\Users\\deepa\\AppData\\Local\\Programs\\Python\\Python39\\msedgedriver.exe")
    driver.implicitly_wait(7)
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

#@pytest.hookimpl(tryfirst=True)
#def pytest_configure(config):
 #   if not os.path.exists("C:\\Users\\deepa\\PycharmProjects1\\AmazonFipkartComboFramework\\Reports"):
  #      os.makedirs("C:\\Users\\deepa\\PycharmProjects1\\AmazonFipkartComboFramework\\Reports")
   # config.option.htmlpath = (
    #    "Reports/" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    #)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)