import time

import constans
from locators.catalog_items_locators import CatalogItemsLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from auth_page import AuthPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SimplePage(BasePage):
    LOGIN_FIELD = (By.XPATH, "//*[@id='search_query_top']")
    PASS_FIELD = (By.XPATH, "//*[@id='search_query_top']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@name='submit_search']")

    def click_to_login_field(self, value):
        field = self.find_element(self.LOGIN_FIELD)
        field.send_keys(value)

    def click_to_password_field(self, value):
        field = self.find_element(self.PASS_FIELD)
        field.send_keys(value)

    def click_submit_button(self):
        button = self.find_element(self.SUBMIT_BUTTON)
        button.click()

    def page_is_exists(self):
        return True


class Site:
    def __init__(self, driver):
        self.auth_page = AuthPage(driver)
        self.simple_page = SimplePage(driver)
