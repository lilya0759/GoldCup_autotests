from .pages.base_page import BasePage
from .pages.main_page import MainPage

link = "https://goldcup24.com/ua/"


def test_user_can_login(browser):
    page = MainPage(browser, link)
    page.open()
    user_login = "l.mazitova@madpie.org"
    user_passw = "123456"
    page.test_go_to_login_form(user_login, user_passw)
