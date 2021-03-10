from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    def authorization_user(self, user_login, user_passw):
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

    def should_be_get_balance(self):
        assert self.is_element_present(
            *MainPageLocators.BALLANCE_ROW), "Строка баланса в шапке сайта не отображается"

    def should_be_get_payment_btn(self):
        assert self.is_element_present(
            *MainPageLocators.PAYMENT_BTN), "Кнопка пополнения баланса в шапке сайта не отображается"

    def should_be_get_payment_out_btn(self):
        assert self.is_element_present(
            *MainPageLocators.PAYMENT_OUT_BTN), "Кнопка вывода в шапке сайта не отображается"

    def should_not_be_get_balance(self):
        assert self.is_not_element_present(
            *MainPageLocators.BALLANCE_ROW), "Строка баланса в шапке сайта отображается"

    def should_not_be_get_payment_btn(self):
        assert self.is_not_element_present(
            *MainPageLocators.PAYMENT_BTN), "Кнопка пополнения баланса в шапке сайта отображается"

    def should_not_be_get_payment_out_btn(self):
        assert self.is_not_element_present(
            *MainPageLocators.PAYMENT_OUT_BTN), "Кнопка вывода в шапке сайта отображается"
