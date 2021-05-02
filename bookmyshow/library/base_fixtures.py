"""Has boiler plate code to reduce code redundancy. Implements
a generator that takes care of set up and tear down"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import BROWSER, URL, CHROME_PATH
opts = Options()
opts.add_experimental_option("useAutomationExtension", False)
opts.add_argument("--start-maximized")


class DriverInit:
    """ class that initialzes webdriver using a generator """
    @staticmethod
    @pytest.fixture(scope="function", autouse=True)
    def init_driver(request):
        """ Generator to initialize webdriver """
        driver = webdriver.Chrome(
            CHROME_PATH, options=opts)
        if BROWSER.lower() == 'firefox':
            driver = webdriver.Firefox()

        driver.get(URL)
        driver.maximize_window()
        request.cls.driver = driver
        yield
        print(driver.title)
        driver.quit()

    @staticmethod
    def sample():
        """Does nothing"""
        print("sample")
