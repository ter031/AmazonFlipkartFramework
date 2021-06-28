import selenium
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains
import time
from utilities.BaseClass import BaseClass
from pageObjects.loginPage import LoginPage
from pageObjects.homePage import HomePage
import pytest

class TestFlipkart(BaseClass):

    def test_SuccessfulLogin(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        loginpage.LoginButton().send_keys("8130253170")
        loginpage.EnterPassword().send_keys("Bilaspur@123")
        loginpage.ClickSubmit().click()
        loggedInVerification = homepage.TextVerification().text
        log.info("My profile added with text"+loggedInVerification)

        assert "My Account" in loggedInVerification




