from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    #Add item to basket
    def get_to_backet(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        login_link.click()

    #Chek correct price after added to backet
    def should_be_true_price(self):
        itemprice = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        basketprice = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert itemprice.text == basketprice.text, 'Uncorrected price in backet'

    #Chek correct item after added to basket
    def should_be_true_item(self):
        itemname = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        itembasketname = self.browser.find_element(*ProductPageLocators.BASKET_ITEM_NAME)
        assert  itemname.text == itembasketname.text, 'Uncorrected item name'

