"""Has generic methods to take care of sending values and clicking elements"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def _wait(func):
    def wrapper(*args, **kwargs):
        driver, element = args
        wait = WebDriverWait(driver, 15)
        loc_type, loc_value = element
        wait.until(EC.visibility_of_element_located((loc_type, loc_value)))
        return func(*args, **kwargs)
    return wrapper


class WebUtils:
    """Has generic methods to take care of sending values and clicking elements"""

    @staticmethod
    # @_wait
    def click_element(driver, element):
        """clicks on the receieved elements"""
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value).click()

    @staticmethod
    def scroll_down(driver):
        """scrolls web page according to direction"""
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()

    @staticmethod
    def scroll_up(driver):
        """scrolls web page according to direction"""
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_UP).perform()
