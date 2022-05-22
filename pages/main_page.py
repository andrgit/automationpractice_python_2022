
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.sign_in_page import SignInPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class MainPage(BasePage):
    URL = "http://automationpractice.com/index.php"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_sign_in_page(self):
        sign_in_btn = self.find_element(MainPageLocators.SIGN_IN_BUTTON)
        sign_in_btn.click()
        return SignInPage(self.driver, self.driver.current_url)

    # def open_email_page(self, email, password):
    #     email_field = self.find_element(MainPageLocators.EMAIL_FIELD_LOCATOR)
    #     email_field.click()
    #     email_field.send_keys(email)
    #     next_btn_email = self.find_element(MainPageLocators.NEXT_BTN_IN_EMAIL_LOCATOR)
    #     next_btn_email.click()
    #     password_field = self.find_element(MainPageLocators.PASSWORD_FIELD_LOCATOR)
    #     time.sleep(3)
    #     password_field.click()
    #     password_field.send_keys(password)
    #     next_btn_password = self.find_element(MainPageLocators.NEXT_BTN_IN_PASSWORD_LOCATOR)
    #     next_btn_password.click()
    #     return EmailPage(self.driver, self.driver.current_url)
