from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the login page')
def open_login_page(context):
    context.app.login_page.open()


@when('Log in to the page')
def log_in(context):
    context.app.login_page.login()


@then('Verify the right page opens')
def verify_page_opens(context):
    context.app.main_page.verify_page_opens()


@when('Filter by sale status of “Out of Stocks”')
def filter_out_of_status(context):
    context.app.main_page.filter_status()


@then('Verify each product contains the Out of Stocks tag')
def verify_products_contains_tag(context):
    context.app.main_page.verify_products_contains_tag()