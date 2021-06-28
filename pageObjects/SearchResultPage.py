from selenium.webdriver.common.by import By

class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver

    SearchResultText = (By.CSS_SELECTOR, "span[class='a-color-state a-text-bold']")

    def VerifySearchResultText(self):
        return self.driver.find_element(*SearchResultPage.SearchResultText)