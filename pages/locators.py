from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (
        By.CSS_SELECTOR, "section.header-wrapper button.button-colorized__transparent-background")
    REGISTER_LINK = (By.CSS_SELECTOR, "section.header-wrapper button")
    LOGIN_INPUT = (
        By.XPATH, "//div[@class='modal-sign-account__userdata']/div/span/input")
    PASSW_INPUT = (
        By.XPATH, "//div[@class='modal-sign-account__userdata']/div[2]/span/input")
    LOGIN_BTN = (By.CSS_SELECTOR, "div.modal-sign-account__userdata button")
    BALLANCE_ROW = (By.CSS_SELECTOR, "div.balance-info")
    BALLANCE_SUM = (By.CSS_SELECTOR, "div.balance-info span:nth-child(2)")
    PAYMENT_BTN = (By.CSS_SELECTOR, "a.button_cash-in")
    PAYMENT_OUT_BTN = (By.CSS_SELECTOR, "a.button_cash-out")
