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