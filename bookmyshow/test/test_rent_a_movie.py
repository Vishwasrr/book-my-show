"""test products availability"""
from library.base_fixtures import DriverInit
from pages.rent_a_movie import RentAMovie

# read = ReadFile()
# element, test_cases = read.read_objects(XL_PATH, BUY_PRODUCT_TESTDATA)


class TestRentAMovie(DriverInit):
    """tests availability of products"""

    # @pytest.mark.parametrize("testcase", test_cases)
    def test_rent_a_movie(self):
        """tests rent a movie"""
        obj = RentAMovie(self.driver)  # pylint:disable=E1101
        self.driver.implicitly_wait(10)   # pylint:disable=E1101
        obj.select_city()
        obj.scroll_down()
        obj.scroll_down()
        obj.scroll_up()
        obj.select_movie()
        obj.click_on_rent()
        obj.click_on_continue()
        print(self.driver.title)   # pylint:disable=E1101
