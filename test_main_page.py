from .pages.base_page import BasePage
from .pages.main_page import MainPage
import pytest

link = "https://goldcup24.com/ua/"

# ------авторизация------


def test_guest_can_see_login_form(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_form()


@pytest.mark.last_marker()
def test_guest_can_close_login_form(browser):
    page = MainPage(browser, link)
    page.open()
    page.open_login_form()
    page.close_login_form()


def test_guest_can_see_login_form_data(browser):
    page = MainPage(browser, link)
    page.open()
    page.open_login_form()
    page.should_be_login_input_in_login_form()
    page.should_be_password_input_in_login_form()
    page.should_be_submit_btn_in_login_form()
    page.should_be_forgot_link_in_login_form()
    page.should_be_vk_btn_in_login_form()
    page.should_be_google_btn_in_login_form()
    page.should_be_ok_btn_in_login_form()
    page.should_be_link_to_change_authorization_form()
    page.should_be_promo_img_in_auth_form()


def test_user_can_login(browser):
    page = MainPage(browser, link)
    page.open()
    user_login = "l.mazitova@madpie.org"
    user_passw = "123456"
    page.auth_user(user_login, user_passw)
    page.should_be_get_balance()
    page.should_be_get_payment_btn()
    page.should_be_get_payment_out_btn()


#  негативные проверки
def test_guest_cant_see_users_elements_in_header(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_not_be_get_balance()
    page.should_not_be_get_payment_btn()
    page.should_not_be_get_payment_out_btn()


# ------регистрация------


def test_user_can_see_register_form(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_register_form()
