from .pages.base_page import BasePage
from .pages.main_page import MainPage

link = "https://goldcup24.com/ua/"


def test_user_can_login(browser):
    page = MainPage(browser, link)
    page.open()
    user_login = "l.mazitova@madpie.org"
    user_passw = "123456"
    page.authorization_user(user_login, user_passw)
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
