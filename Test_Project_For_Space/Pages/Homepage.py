from selenium.webdriver.common.by import By
from Config.Config import TestWeb
from Pages.function import WebPage


class HomePage(WebPage):

    """

        Homepage testing class

    """

    """ Variable for xpath """
    search_bar = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/div[1]/div/div[2]/div/div/div')
    search_input = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/div[1]/div/div[2]/div/div/div/form/input')
    header_bar = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/header/section/div[2]/div/nav')
    navigation_bar = (By.XPATH, '//*[@id="mount"]/div/div[2]/div[2]/div/div/div/div/main/div/div/section[1]/div/ul')
    search_result = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/main/div/div/div[1]/div/div[2]/div/div/ul/li[2]/a')

    """ This is page action functions """

    def __init__(self, driver):
        """ constructor for the class """
        super().__init__(driver)
        self.driver.get(TestWeb.BASE_URL)

    def get_homepage_title(self, title):
        """ This is used to get the page title """
        return self.get_title(title)

    def is_searchbar_exist(self):
        """ This is used to check search availability """
        return self.is_visible(self.search_bar)

    def is_header_exist(self):
        """ This is used to check header menu availability """
        return self.is_visible(self.header_bar)

    def is_navigation_exist(self):
        """ This is used to check navigation menu availability """
        return self.is_visible(self.navigation_bar)

    def do_search(self, search):
        """ Test Search By Use """
        self.do_send_keys(self.search_input, search)
        self.action_click(self.search_result)
