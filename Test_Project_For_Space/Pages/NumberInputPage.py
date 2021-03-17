import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from Config.Config import TestWeb
from Pages.function import WebPage


class InputPage(WebPage):

    """

    This Class is for number input and checking page

    """

    """Variables for Xpath"""
    num_input_field = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div/div[2]/form/div/input')
    num_check_button = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div/div[2]/form/button')
    Options_Menu = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[2]/div[2]/div/div/label')
    Item_Pick = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[2]/div[2]/div/div/div/a[3]')
    Checkout_Button = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/main/section/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/button[2]')
    Pay_Button = (By.XPATH, '/html/body/div/div[1]/div/div/div/form/div[2]/button')
    Ecommerce = (By.XPATH, '/html/body')

    """This is page action functions """

    def __init__(self, driver):
        """ Constructor for the class """
        super().__init__(driver)
        self.driver.get(TestWeb.NUMBER_CHECK_URL)

    def is_input_exist(self):
        """ This checking input bar """
        return self.is_visible(self.num_input_field)

    def is_button_exist(self):
        """ This checks number check button """
        return self.is_visible(self.num_check_button)

    def do_number_check(self, number):
        """This input phone number and use check button """
        self.do_send_keys(self.num_input_field, number)
        self.action_click(self.num_check_button)

    def is_ecommerce_exist(self):
        """ This function checks ecommerce page"""
        return self.is_visible(self.Ecommerce)
