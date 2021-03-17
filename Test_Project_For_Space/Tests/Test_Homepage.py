import allure
from allure_commons.types import AttachmentType
from Config.Config import TestWeb
from Pages.Homepage import HomePage
from Pages.function import WebPage
from Tests.test_function import BaseTest


@allure.severity(allure.severity_level.NORMAL)
class Test_Homepage(BaseTest):

    """

    This class contains test functions for homepage

    """

    @allure.severity(allure.severity_level.MINOR)
    def test_searchbar_visible(self):
        """ Test function for searchbar availability """
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_searchbar_exist()
        allure.attach(self.driver.get_screenshot_as_png(), name="test_search_bar", attachment_type=AttachmentType.PNG)
        assert flag

    @allure.severity(allure.severity_level.MINOR)
    def test_header_visible(self):
        """ Test function for header availability """
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_header_exist()
        allure.attach(self.driver.get_screenshot_as_png(), name="test_header", attachment_type=AttachmentType.PNG)
        assert flag

    @allure.severity(allure.severity_level.MINOR)
    def test_navigation_visible(self):
        """ Test function for navigation availability """
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_navigation_exist()
        allure.attach(self.driver.get_screenshot_as_png(), name="test_navigation", attachment_type=AttachmentType.PNG)
        assert flag

    @allure.severity(allure.severity_level.NORMAL)
    def test_search_usage(self):
        """ Test function for search usage """
        self.homePage = HomePage(self.driver)
        self.webPage = WebPage(self.driver)
        self.homePage.do_search(TestWeb.TestSearchWord)
        flag = self.webPage.action_click(HomePage.search_result)
        allure.attach(self.driver.get_screenshot_as_png(), name="test_search_usage", attachment_type=AttachmentType.PNG)
        assert flag
