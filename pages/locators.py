from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group > .btn:nth-child(1)")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
    ITEM_NAME = (By.CSS_SELECTOR, ".breadcrumb > .active")
    BASKET_ITEM_NAME = (By.XPATH, "//div[@id='messages']//strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages >.alert-success:nth-child(1)")

class BasketPageLocators():
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_IS_NOT_EMPTY = (By.CSS_SELECTOR, "#content_inner > .basket-title")