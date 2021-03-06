import selenium
from selenium.webdriver.chrome.webdriver import WebDriver
from utilities.BaseClass import BaseClass1
import pytest
from pageObjects.HomePageAmazon import HomePageAmazon
from pageObjects.MobileSearchResultPageAmazon import MobileSearchResultPageAmazon
from pageObjects.SearchResultPage import SearchResultPage

class TestAmazon(BaseClass1):

    def test_searchResultVerification(self):
        log = self.getLogger()
        homepageamazon = HomePageAmazon(self.driver)
        searchresultpage = SearchResultPage(self.driver)
        homepageamazon.EnterSearchCriteria().send_keys("digital watches")
        homepageamazon.ClickSearchButton().click()
        ResultsText = searchresultpage.VerifySearchResultText().text
        log.info("searched keywords verified as "+ ResultsText)

        assert "digital watches" in ResultsText

    def test_AccessToCanadaPortal(self):
        log = self.getLogger()
        homepageamazon = HomePageAmazon(self.driver)
        homepageamazon.ClickCanadaPortalLink().click()
        AmazonCanadaPortal = self.driver.current_url
        log.info("URL to Canada portal is "+ AmazonCanadaPortal)

        assert AmazonCanadaPortal == "https://www.amazon.ca/ref=footer_ca"

    def test_VerifyProductTextInSearchResults(self):
        log = self.getLogger()
        homepageamazon = HomePageAmazon(self.driver)
        mobilesearchresultpage = MobileSearchResultPageAmazon(self.driver)
        homepageamazon.ClickMobilesLink().click()
        mobilesearchresultpage.ClickOnePlusCheckbox().click()
        OneplusProducts = mobilesearchresultpage.VerifyProductsOnPage()

        for OneplusProduct in OneplusProducts:
            ProductText = OneplusProduct.text
            assert "OnePlus" in ProductText
        log.info("OnePlus is there in every product's text")