from pages.login_page import LoginPage
from pages.base_page import Page
from pages.main_page import MainPage


class Application:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
