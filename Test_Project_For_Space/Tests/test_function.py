import pytest
from selenium import webdriver

from Config.Config import TestWeb


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    """

    This class is for locate and pick up webdriver for selenium

    """

    @pytest.fixture(params=["chrome"], scope='class')
    def init_driver(self, request):
        global web_driver
        if request.param == "chrome":
            web_driver = webdriver.Chrome(executable_path=TestWeb.CHROME_EXECUTABLE_PATH)
        if request.param == "firefox":
            web_driver = webdriver.Chrome(executable_path=TestWeb.CHROME_EXECUTABLE_PATH)
        request.cls.driver = web_driver
        yield
        web_driver.close()
