from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import faker
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is absent in current url"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        pass_input = self.browser.find_element(*LoginPageLocators.PASS1_INPUT)
        pass_confirm = self.browser.find_element(*LoginPageLocators.PASS2_INPUT)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_input.send_keys(email)
        pass_input.send_keys(password)
        pass_confirm.send_keys(password)
        reg_button.click()

    def make_email_and_pass(self):
        # make a login and parol for user
        return (str(time.time()) + "@fakemail.org", "RandomParol123")


