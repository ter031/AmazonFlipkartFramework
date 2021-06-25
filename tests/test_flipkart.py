from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains
import time
from utilities.BaseClass import BaseClass

class TestFlipkart(BaseClass):

    def test_SuccessfulLogin(self):
        self.driver.find_element_by_css_selector("input[class='_2IX_2- VJZDxU']").send_keys("8130253170")
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys("Bilaspur@123")
        self.driver.find_element_by_xpath("//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
        loggedInVerification = self.driver.find_element_by_xpath(
            "//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div").text

        assert "My Account" in loggedInVerification

    def test_FailedLogin(self):
        self.driver.find_element_by_css_selector("input[class='_2IX_2- VJZDxU']").send_keys("8130253170")
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys("abc@123")
        self.driver.find_element_by_xpath("//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
        failedLoginMessage = self.driver.find_element_by_css_selector("span[class='_2YULOR'] span").text

        assert "Your username or password is incorrect" == failedLoginMessage

    def test_AccesToProfile(self):
        self.driver.find_element_by_css_selector("input[class='_2IX_2- VJZDxU']").send_keys("8130253170")
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys("Bilaspur@123")
        self.driver.find_element_by_xpath("//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
        action = ActionChains(driver)
        menu = self.driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div")
        action.move_to_element(menu).perform()
        self.driver.find_element_by_xpath(
            "//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul/li[1]/a").click()
        ProfilePageURL = self.driver.current_url
        assert ProfilePageURL == "https://www.flipkart.com/account/?rd=0&link=home_account"
