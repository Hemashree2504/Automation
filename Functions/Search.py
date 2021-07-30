import pytest
from selenium.webdriver.common.keys import Keys

from Functions.WebDriverHelper import WebDriverHelper


class Search(WebDriverHelper):

    def __init__(self):
        WebDriverHelper.__init__(self)
        self.Search = None
        self.Close = None
        self.Search_button = None
        self.Cart = None

    def click_search(self, search):
        close_button = "//button[contains(text(),'✕')]"
        search_xpath = "//input[@type='text']"

        try:
            self.Close = self.find_element('xpath', close_button, 10)
            self.Close.click()
            self.Search = self.find_element('xpath', search_xpath, 20)
            self.Search.send_keys(search)
            self.Search.send_keys(Keys.ENTER)

        except BaseException as ex:
            pytest.fail("unable to search", ex)

    def search_product_name(self):
        search_product_name = "//div[contains(text(),'SAMSUNG Galaxy F12 (s Green, 128 GB)')]"

        try:
            self.Search_button = self.find_element  ('xpath', search_product_name, 50)
            # self.move_to_element(self.Search_button)
            self.Search_button.click()

        except BaseException as ex:
            pytest.fail("unable to search", ex)

    def add_to_cart(self):
        cart_button_xpath = "//li/button"

        try:
            self.switch_to_window(1)
            self.Cart = self.find_element('xpath', cart_button_xpath, 10)
            self.Cart.click()

        except BaseException as ex:
            pytest.fail("unable to add to cart", ex)
