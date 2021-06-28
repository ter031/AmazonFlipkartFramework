from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    loginButton = (By.CSS_SELECTOR, "input[class='_2IX_2- VJZDxU']")
    passwordBox = (By.XPATH, "//input[@type='password']")
    submitButton = (By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
    failedTextLogin = (By.CSS_SELECTOR, "span[class='_2YULOR'] span")
    forgetPasswordLink = (By.LINK_TEXT, "Forgot?")

    def LoginButton(self):
        return self.driver.find_element(*LoginPage.loginButton)

    def EnterPassword(self):
        return self.driver.find_element(*LoginPage.passwordBox)

    def ClickSubmit(self):
        return self.driver.find_element(*LoginPage.submitButton)

    def VerifyFailedLoginText(self):
        return self.driver.find_element(*LoginPage.failedTextLogin)

    def ClickForgetPasswordLink(self):
        return self.driver.find_element(*LoginPage.forgetPasswordLink)