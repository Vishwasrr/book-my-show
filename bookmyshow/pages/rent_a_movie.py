"""automates renting a movie"""
from time import sleep
from library.web_utils import WebUtils
from library.file_library import ReadFile
# from selenium import webdriver
# from config import XL_PATH, RENT_TICKET_LOCS, CHROME_PATH, URL
read = ReadFile()
element, keys = read.read_objects(XL_PATH, RENT_TICKET_LOCS)
web = WebUtils()


class RentAMovie:
    """automates renting a movie"""

    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self):
        """scrolls down"""
        web.scroll_down(self.driver)

    def scroll_up(self):
        """scrolls down"""
        web.scroll_up(self.driver)

    def select_city(self):
        """selects city"""
        web.click_element(self.driver, element['select_city'])

    def select_movie(self):
        """selects movie"""
        web.click_element(self.driver, element['select_movie'])

    def click_on_rent(self):
        """selects rent option"""
        web.click_element(self.driver, element['click_on_rent'])

    def click_on_continue(self):
        """clicks on continue"""
        web.click_element(self.driver, element['click_on_continue'])


# driver = webdriver.Chrome(CHROME_PATH)
# driver.get(URL),
# driver.implicitly_wait(15)
# obj = RentAMovie(driver)
# obj.select_city()
# # sleep(2.5)
# obj.scroll_down()
# obj.scroll_down()
# obj.scroll_up()
# obj.select_movie()
# obj.click_on_rent()
# obj.click_on_continue()

# driver.find_element_by_xpath("//img[@alt='BANG']").click()  # select bangalore
# action = ActionChains(driver)
# action.send_keys(Keys.PAGE_DOWN)
# # select Tom and Jerry movie
# driver.find_element_by_xpath("//img[@alt='Tom & Jerry']").click()
# driver.find_element_by_xpath(
#     "//button").click()  # click on rent

# driver.find_element_by_xpath("//span[text()='Continue']").click()
