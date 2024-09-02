from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select


from pages.base_page import Page


class MainPage(Page):
    PAGE_TITLE_TXT = (By.CSS_SELECTOR, '.page-title.off_plan')
    SALE_STATUS_BTN = (By.ID, 'Location-2')
    OUT_OF_STATUS_TAG = (By.XPATH, "//div[@wized='projectStatus']")
    PRODUCT_NUMBERS = (By.CSS_SELECTOR, ".properties-counter")

    def verify_page_opens(self):
        actual_text = self.driver.find_element(*self.PAGE_TITLE_TXT).text
        expected_text = 'Total projects'
        assert expected_text in actual_text, f'Expected {expected_text} not in actual {actual_text}'

    def filter_status(self):
        select_element = self.driver.find_element(*self.SALE_STATUS_BTN)
        select = Select(select_element)
        sleep(5)
        select.select_by_visible_text("Out of stock")
        sleep(5)

    def verify_products_contains_tag(self):
        tags = self.driver.find_elements(*self.OUT_OF_STATUS_TAG)
        tags_counts = 0

        for tag in tags:
            if tag.text == 'Out of stock':
                tags_counts += 1

        assert tags_counts == 24, f'Expected 24 out of stock, got {tags_counts}'