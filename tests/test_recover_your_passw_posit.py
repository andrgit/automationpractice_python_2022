import allure
import pytest

import constans
from pages.main_page import MainPage


@allure.story("Password recovery test - positive scenario")
def test_recover_your_password(driver):
    """
    Password recovery test
    """
    your_email = constans.EMAIL_LOGIN
    page = MainPage(driver)
    with allure.step('Open main page'):
        page.open()
    with allure.step('Open sign-in page'):
        login_page = page.open_sign_in_page()
    with allure.step('Click to Forgot your password'):
        forgot_password_page = login_page.forgot_your_passw_link()
        retrieve_password = forgot_password_page.recover_user_passw(your_email)
    assert "confirmation email has been sent" in \
           retrieve_password[0].text, "Problem with recovery password"
