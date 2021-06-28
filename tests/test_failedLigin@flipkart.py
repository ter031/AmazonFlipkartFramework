import selenium
from utilities.BaseClass import BaseClass
from pageObjects.loginPage import LoginPage
import pytest

class TestFailedLogin(BaseClass):
    def test_FailedLogin(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        loginpage.LoginButton().send_keys("8130253170")
        loginpage.EnterPassword().send_keys("abc@123")
        loginpage.ClickSubmit().click()
        failedLoginMessage = loginpage.VerifyFailedLoginText().text
        log.info("failed login message is"+failedLoginMessage)

        assert "Your username or password is incorrect" == failedLoginMessage