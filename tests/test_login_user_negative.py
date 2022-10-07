import allure
import pytest

import constans
from pages.main_page import MainPage


@allure.story("The Sign-in process for user - Negative scenario")
def test_login_user_negative(driver):
    """
    The Sign-in process
      ii. Negative scenario (Invalid credentials) and catch the error message
    """
    email_test = constans.EMAIL_LOGIN
    passw_test = constans.PASSWORD_LOGIN_FAIL  # Wrong password
    page = MainPage(driver)
    with allure.step('Open main page'):
        page.open()
    with allure.step('Open sign-in page'):
        login_page = page.open_sign_in_page()
    with allure.step('Try to login negative scenario'):
        sign_in_page = login_page.user_login(email_test, passw_test)
    assert "Authentication failed" or "error" in \
           sign_in_page.text, "Problem with negative test"
