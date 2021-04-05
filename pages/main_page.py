from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    # авторизация
    def open_login_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        time.sleep(3)

    def close_login_form(self):
        close_btn = self.browser.find_element(*MainPageLocators.CLOSE_BNT)
        close_btn.click()
        time.sleep(3)

    def should_be_login_form(self):
        self.open_login_form()
        assert self.is_element_present(
            *MainPageLocators.AUTORISATION_FORM), "Поп-ап авторизации не отображается"

    def should_be_login_input_in_login_form(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_INPUT), "Не отображается поле для ввода емаила"

    def should_be_password_input_in_login_form(self):
        assert self.is_element_present(
            *MainPageLocators.PASSW_INPUT), "Не отображается поле для ввода пароля"

    def should_be_submit_btn_in_login_form(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_BTN), "Не отображается кнопка подтверждения данных"

    def should_be_forgot_link_in_login_form(self):
        assert self.is_element_present(
            *MainPageLocators.FORGOT_PASSW_LINK), "Не отображается ссылка для восстановления пароля"

    def should_be_vk_btn_in_login_form(self):
        assert self.is_element_present(
            *MainPageLocators.VK_BTN), "Не отображается кнока авторизации через ВК"

    def should_be_google_btn_in_login_form(self):
        assert self.is_element_present(
            *MainPageLocators.GOOGLE_BTN), "Не отображается кнока авторизации через GOOGLE"

    def should_be_ok_btn_in_login_form(self):
        assert self.is_element_present(
            *MainPageLocators.OK_BTN), "Не отображается кнока авторизации через OK"

    def should_be_link_to_change_authorization_form(self):
        assert self.is_element_present(
            *MainPageLocators.REGISTER_LINK_IN_LOGIN_FORM), "Не отображается ссылка для прехода к смене формы авторизации"

    def should_be_promo_img_in_auth_form(self):
        assert self.is_element_present(
            *MainPageLocators.PROMO_IMG_IN_AUTH_FORM), "Не отображается изображение в поп-апе авторизации"

    def auth_user(self, user_login, user_passw):
        self.open_login_form()
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

    def open_restore_link(self):
        restore_link = self.browser.find_element(
            *MainPageLocators.FORGOT_PASSW_LINK)
        restore_link.click()
        time.sleep(2)

    def go_to_auth_by_vk(self):
        self.browser.find_element(*MainPageLocators.VK_BTN).click()
        time.sleep(2)

    def go_to_auth_by_ok(self):
        self.browser.find_element(*MainPageLocators.OK_BTN).click()
        time.sleep(2)

    def go_to_auth_by_google(self):
        self.browser.find_element(*MainPageLocators.GOOGLE_BTN).click()
        time.sleep(2)
    # регистрация

    def open_register_form(self):
        register_form = self.browser.find_element(
            *MainPageLocators.REGISTER_LINK)
        register_form.click()
        time.sleep(3)
