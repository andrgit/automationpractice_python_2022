from selenium.webdriver.support.wait import WebDriverWait

from locators.login_page_locators import LoginPageLocators
from locators.registration_page_locators import RegistrationPageLocators
from locators.sign_in_page_locators import SignInPageLocators
from pages.base_page import BasePage
from pages.create_user_page import CreateUserPage
from pages.forgot_password_page import ForgotPasswPage
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(BasePage):
    def user_create_account(self, email):
        email_field = self.find_element(
            SignInPageLocators.EMAIL_FIELD_CREATE_ACCOUNT)
        email_field.send_keys(email)
        create_account_btn = self.find_element(
            SignInPageLocators.CREATE_AN_ACCOUNT_BTN)
        create_account_btn.click()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    RegistrationPageLocators.ACCOUNT_CREATION_FORM))
            return CreateUserPage(self.driver, self.driver.current_url)
        except:
            create_account_failed = self.find_element(
                SignInPageLocators.ERROR_LOGIN_REGISTERED)
            return create_account_failed, (
                self.driver, self.driver.current_url)

    def user_login(self, email, passw):
        email_field = self.find_element(SignInPageLocators.EMAIL_FIELD_LOG_IN)
        email_field.send_keys(email)
        passw_field = self.find_element(SignInPageLocators.PASSW_FIELD_LOG_IN)
        passw_field.send_keys(passw)
        sign_in_btn = self.find_element(SignInPageLocators.SIGN_IN_BTN_LOGIN)
        sign_in_btn.click()
        sign_in_result = self.find_elements(
            LoginPageLocators.WELCOME_TO_ACCOUNT_TEXT and
            SignInPageLocators.FAIL_LOGIN_MESSG)
        if "Authentication failed" in sign_in_result[0].text:
            return sign_in_result, LoginPage(self.driver,
                                             self.driver.current_url)
        elif "Welcome to your account" in sign_in_result[0].text:
            return sign_in_result, LoginPage(self.driver,
                                             self.driver.current_url)

    def forgot_your_passw_link(self):
        forgot_password_btn = self.find_element(
            SignInPageLocators.FORGOT_YOUR_PASSW_LINK2)
        forgot_password_btn.click()
        return ForgotPasswPage(self.driver,
                               self.driver.current_url)
