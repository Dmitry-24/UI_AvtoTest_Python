from pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("bugged_link", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.get_to_backet()
    page.solve_quiz_and_get_code()
    page.should_be_true_item()

