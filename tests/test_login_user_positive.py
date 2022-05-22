import allure
import pytest

import constans
from pages.main_page import MainPage


@allure.story("The Sign-in process for user - positive scenario")
def test_login_user_positive(driver):
    """
    The Sign-in process
      i. Positive scenario (Valid credentials)
    """
    email_test = constans.EMAIL_LOGIN
    passw_test = constans.PASSWORD_LOGIN
    page = MainPage(driver)
    with allure.step('Open main page'):
        page.open()
    with allure.step('Open sign-in page'):
        login_page = page.open_sign_in_page()
    with allure.step('Try to login positive'):
        sign_in_page = login_page.user_login(email_test, passw_test)
    assert "Welcome to your account" in sign_in_page[0].text, "Problem with positive test"
