import selenium
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains
import time
from utilities.BaseClass import BaseClass
from pageObjects.loginPageflipkart import LoginPage
from pageObjects.homePageflipkart import HomePage
import pytest
from TestData.LoginPageDataFlipkart import LoginPageDataFlipkart

class TestFlipkart(BaseClass):

    def test_SuccessfulLogin(self, getDataValidCredentials):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        loginpage.LoginButton().send_keys(getDataValidCredentials["EnterEmailOrMobNumber"])
        loginpage.EnterPassword().send_keys(getDataValidCredentials["EnterPassword"])
        loginpage.ClickSubmit().click()
        loggedInVerification = homepage.TextVerification().text
        log.info("My profile added with text "+ loggedInVerification)

        assert "My Account" in loggedInVerification

    @pytest.fixture(params=LoginPageDataFlipkart.getTestValidCredentials("testcase1"))
    def getDataValidCredentials(self, request):
        return request.param

    def test_forgetPassword(self, getDataForgetPassword):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        loginpage.LoginButton().send_keys(getDataForgetPassword["EnterEmailOrMobNumber"])
        loginpage.ClickForgetPasswordLink().click()
        log.info("OTP for resetting password received")

    @pytest.fixture(params=LoginPageDataFlipkart.test_NumberForgetPassword)
    def getDataForgetPassword(self, request):
        return request.param

    def test_AccesToProfile(self, getDataValidCredentials):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        loginpage.LoginButton().send_keys(getDataValidCredentials["EnterEmailOrMobNumber"])
        loginpage.EnterPassword().send_keys(getDataValidCredentials["EnterPassword"])
        loginpage.ClickSubmit().click()
        action = ActionChains(self.driver)
        menu = homepage.AllMenuItems()
        action.move_to_element(menu).perform()
        homepage.ClickMyProfileLink().click()
        ProfilePageURL = self.driver.current_url
        log.info("profile page url is verified as "+ ProfilePageURL)

        assert ProfilePageURL == "https://www.flipkart.com/account/?rd=0&link=home_account"

    def test_FailedLogin(self, getDataInvalidCredentials):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        loginpage.LoginButton().send_keys(getDataInvalidCredentials["EnterEmailOrMobNumber"])
        loginpage.EnterPassword().send_keys(getDataInvalidCredentials["EnterPassword"])
        loginpage.ClickSubmit().click()
        failedLoginMessage = loginpage.VerifyFailedLoginText().text
        log.info("failed login message is "+ failedLoginMessage)

        assert "Your username or password is incorrect" == failedLoginMessage

    @pytest.fixture(params=LoginPageDataFlipkart.test_InvalidloginCredentials)
    def getDataInvalidCredentials(self, request):
        return request.param





