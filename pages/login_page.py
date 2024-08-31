from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class LoginPage(Page):
    E_MAIL = (By.ID, 'email-2')
    PASSWORD = (By.ID, 'field')
    LOGIN_BTN = (By.CSS_SELECTOR, '.login-button.w-button')

    def open(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def login(self):
        self.input_text('sedat_tilev@outlook.com', *self.E_MAIL)
        self.input_text('Sedat.1905', *self.PASSWORD)
        self.click(*self.LOGIN_BTN)
