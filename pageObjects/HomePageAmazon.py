from selenium.webdriver.common.by import By

class HomePageAmazon:
    def __init__(self, driver):
        self.driver = driver

    SearchBox = (By.ID, "twotabsearchtextbox")
    SearchButton = (By.ID, "nav-search-submit-button")

    def EnterSearchCriteria(self):
        return self.driver.find_element(*HomePageAmazon.SearchBox)

    def ClickSearchButton(self):
        return self.driver.find_element(*HomePageAmazon.SearchButton)