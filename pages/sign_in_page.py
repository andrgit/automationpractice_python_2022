from locators.login_page_locators import LoginPageLocators
from locators.sign_in_page_locators import SignInPageLocators
from pages.base_page import BasePage
import constans
from pages.create_user_page import CreateUserPage
from pages.login_page import LoginPage


class SignInPage(BasePage):
    def try_to_create_account(self):
        email_field = self.find_element(SignInPageLocators.EMAIL_FIELD_CREATE_ACCOUNT)
        email_field.send_keys(constans.EMAIL_LOGIN)
        create_account_btn = self.find_element(SignInPageLocators.CREATE_AN_ACCOUNT_BTN)
        create_account_btn.click()
        return CreateUserPage(self.driver, self.driver.current_url)

    def try_to_login(self, email, passw):
        email_field = self.find_element(SignInPageLocators.EMAIL_FIELD_LOG_IN)
        email_field.send_keys(email)
        passw_field = self.find_element(SignInPageLocators.PASSW_FIELD_LOG_IN)
        passw_field.send_keys(passw)
        sign_in_btn = self.find_element(SignInPageLocators.SIGN_IN_BTN_LOGIN)
        sign_in_btn.click()
        sign_in_success = self.find_element(LoginPageLocators.WELCOME_TO_ACCOUNT_TEXT)
        if sign_in_success:
            return sign_in_success, LoginPage(self.driver, self.driver.current_url)
        else:
            sign_in_failed = self.find_element(SignInPageLocators.FAIL_LOGIN_MESSG)
            return sign_in_failed, LoginPage(self.driver, self.driver.current_url)
