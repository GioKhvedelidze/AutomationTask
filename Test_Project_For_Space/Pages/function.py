from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebPage:

    """

       This class contains useful functions for testing

    """

    def __init__(self, driver):
        """ constructor for the class """
        self.driver = driver

    def action_await_click(self, by_locator):
        """ This is a Click function Works until Become clickable """
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    def action_click(self, by_locator):
        """ This is a function for click buttons """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        """ This is a function for give our input to the website """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        """ This is a function for pick up text from selected element """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        """ This is a function for checking element availability """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        """ This is a function for pick up page titles """
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
