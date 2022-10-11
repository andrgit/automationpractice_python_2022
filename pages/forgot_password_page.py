from locators.forgot_passw_page_locators import ForgotPasswPageLocators
from pages.base_page import BasePage


class ForgotPasswPage(BasePage):
    def recover_user_passw(self, email):
        email_address_field = self.find_element(
            ForgotPasswPageLocators.email_field)
        email_address_field.send_keys(email)
        retrieve_password_btn = self.find_element(
            ForgotPasswPageLocators.retrieve_password_btn)
        retrieve_password_btn.click()
        confirm_recovery_passw = self.find_element(
            ForgotPasswPageLocators.confirm_message)
        return confirm_recovery_passw, ForgotPasswPage(self.driver,
                                                       self.driver.current_url)
