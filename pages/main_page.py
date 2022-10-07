from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.sign_in_page import SignInPage


class MainPage(BasePage):
    URL = "http://automationpractice.com/index.php"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_sign_in_page(self):
        sign_in_btn = self.find_element(MainPageLocators.SIGN_IN_BUTTON)
        sign_in_btn.click()
        return SignInPage(self.driver, self.driver.current_url)
