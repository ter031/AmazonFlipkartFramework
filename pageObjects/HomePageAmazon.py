from selenium.webdriver.common.by import By

class HomePageAmazon:
    def __init__(self, driver):
        self.driver = driver

    SearchBox = (By.ID, "twotabsearchtextbox")
    SearchButton = (By.ID, "nav-search-submit-button")
    CanadaPortalLink = (By.LINK_TEXT, "Canada")
    MobilesLink = (By.LINK_TEXT, "Mobiles")

    def EnterSearchCriteria(self):
        return self.driver.find_element(*HomePageAmazon.SearchBox)

    def ClickSearchButton(self):
        return self.driver.find_element(*HomePageAmazon.SearchButton)

    def ClickCanadaPortalLink(self):
        return self.driver.find_element(*HomePageAmazon.CanadaPortalLink)

    def ClickMobilesLink(self):
        return self.driver.find_element(*HomePageAmazon.MobilesLink)