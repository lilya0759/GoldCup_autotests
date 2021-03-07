from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    def test_go_to_login_form(self, user_login, user_passw):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        time.sleep(5)
        login = self.browser.find_element(*MainPageLocators.LOGIN_INPUT)
        login.send_keys(user_login)
        passw = self.browser.find_element(*MainPageLocators.PASSW_INPUT)
        passw.send_keys(user_passw)
        login_btn = self.browser.find_element(*MainPageLocators.LOGIN_BTN)
        login_btn.click()
        time.sleep(5)
