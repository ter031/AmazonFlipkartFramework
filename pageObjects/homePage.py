from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    AccountVerificationText = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div")
    MenuItems = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div")
    MyProfileLink = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[3]/div/div/div[2]/div[2]/div/ul/li[1]/a")

    def TextVerification(self):
        self.driver.find_element(*HomePage.AccountVerificationText)

    def AllMenuItems(self):
        self.driver.find_element(*HomePage.MenuItems)

    def ClickMyProfileLink(self):
        self.driver.find_element(*HomePage.MyProfileLink)