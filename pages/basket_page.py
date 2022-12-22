from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "Items in basket, but should not be"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY), \
            "Items in basket, but should not be"