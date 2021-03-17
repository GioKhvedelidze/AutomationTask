from allure_commons.types import AttachmentType
import allure
from Config.Config import TestWeb
from Pages.NumberInputPage import InputPage
from Tests.test_function import BaseTest


@allure.severity(allure.severity_level.NORMAL)
class Test_NumInput(BaseTest):

    """

    This class conntains test functions for mobile number input page

    """

    @allure.severity(allure.severity_level.CRITICAL)
    def test_input_exist(self):
        """ Test Number Input Field Availability """
        self.inputPage = InputPage(self.driver)
        flag = self.inputPage.is_input_exist()
        allure.attach(self.driver.get_screenshot_as_png(), name="test_input_exist", attachment_type=AttachmentType.PNG)
        assert flag

    @allure.severity(allure.severity_level.CRITICAL)
    def test_button_exist(self):
        """ Test Check Button Availability """
        self.inputPage = InputPage(self.driver)
        flag = self.inputPage.is_button_exist()
        allure.attach(self.driver.get_screenshot_as_png(), name="test_button_exist", attachment_type=AttachmentType.PNG)
        assert flag

    @allure.severity(allure.severity_level.NORMAL)
    def test_number_check(self):
        """ Test Number Checking Button """
        self.inputPage = InputPage(self.driver)
        self.inputPage.do_number_check(TestWeb.TestPhoneNumber)
        self.inputPage.action_click(InputPage.Options_Menu)
        allure.attach(self.driver.get_screenshot_as_png(), name="test_number_check", attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.NORMAL)
    def test_payment(self):
        """ Test Payment button """
        self.inputPage = InputPage(self.driver)
        self.inputPage.do_number_check(TestWeb.TestPhoneNumber)
        self.inputPage.action_click(InputPage.Options_Menu)
        self.inputPage.action_click(InputPage.Item_Pick)
        self.inputPage.action_click(InputPage.Checkout_Button)
        allure.attach(self.driver.get_screenshot_as_png(), name="test_payment", attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.NORMAL)
    def test_ecommerce_page(self):
        """ Test ecommerce checkout page """
        self.inputPage = InputPage(self.driver)
        self.inputPage.do_number_check(TestWeb.TestPhoneNumber)
        self.inputPage.action_click(InputPage.Options_Menu)
        self.inputPage.action_click(InputPage.Item_Pick)
        self.inputPage.action_click(InputPage.Checkout_Button)
        allure.attach(self.driver.get_screenshot_as_png(), name="test_ecommerce", attachment_type=AttachmentType.PNG)
        self.inputPage.is_ecommerce_exist()
