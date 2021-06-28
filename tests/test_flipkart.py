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
        log.info("My profile added with text "+ loggedInVerification)

        assert "My Account" in loggedInVerification

    def test_forgetPassword(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        loginpage.LoginButton().send_keys("8130253170")
        loginpage.ClickForgetPasswordLink().click()
        log.info("OTP for resetting password received")

    def test_AccesToProfile(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        loginpage.LoginButton().send_keys("8130253170")
        loginpage.EnterPassword().send_keys("Bilaspur@123")
        loginpage.ClickSubmit().click()
        action = ActionChains(self.driver)
        menu = homepage.AllMenuItems()
        action.move_to_element(menu).perform()
        homepage.ClickMyProfileLink().click()
        ProfilePageURL = self.driver.current_url
        log.info("profile page url is verified as "+ ProfilePageURL)

        assert ProfilePageURL == "https://www.flipkart.com/account/?rd=0&link=home_account"

    def test_FailedLogin(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        loginpage.LoginButton().send_keys("8130253170")
        loginpage.EnterPassword().send_keys("abc@123")
        loginpage.ClickSubmit().click()
        failedLoginMessage = loginpage.VerifyFailedLoginText().text
        log.info("failed login message is "+ failedLoginMessage)

        assert "Your username or password is incorrect" == failedLoginMessage





