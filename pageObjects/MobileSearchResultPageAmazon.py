from selenium.webdriver.common.by import By

class MobileSearchResultPageAmazon:
    def __init__(self, driver):
        self.driver = driver


    OnePlusCheckbox = (By.XPATH, "//*[@id='s-refinements']/div[5]/ul/li[3]/span/a/div/label/i")
    ProductsOnPage = (By.XPATH, "//div[@class='s-expand-height s-include-content-margin s-latency-cf-section {{ borderCssClass }}']/div/div/div/h2")


    def ClickOnePlusCheckbox(self):
        return self.driver.find_element(*MobileSearchResultPageAmazon.OnePlusCheckbox)

    def VerifyProductsOnPage(self):
        return self.driver.find_elements(*MobileSearchResultPageAmazon.ProductsOnPage)