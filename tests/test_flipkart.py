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
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        loginpage.LoginButton().send_keys("8130253170")
        loginpage.EnterPassword().send_keys("Bilaspur@123")
        loginpage.ClickSubmit().click()
        loggedInVerification = homepage.TextVerification().text

        assert "My Account" in loggedInVerification

    def test_FailedLogin(self):
        loginpage = LoginPage(self.driver)
        loginpage.LoginButton().send_keys("8130253170")
        loginpage.EnterPassword().send_keys("abc@123")
        loginpage.ClickSubmit().click()
        failedLoginMessage = loginpage.VerifyFailedLoginText().text

        assert "Your username or password is incorrect" == failedLoginMessage

    def test_AccesToProfile(self):
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        loginpage.LoginButton().send_keys("8130253170")
        loginpage.EnterPassword().send_keys("Bilaspur@123")
        loginpage.ClickSubmit().click()
        action = ActionChains(driver)
        menu = homepage.AllMenuItems()
        action.move_to_element(menu).perform()
        homepage.ClickMyProfileLink().click()
        ProfilePageURL = self.driver.current_url

        assert ProfilePageURL == "https://www.flipkart.com/account/?rd=0&link=home_account"
