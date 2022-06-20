import allure

import constans
from pages.main_page import MainPage


@allure.story("Create new user")
def test_create_new_user(driver):
    """
    The signup Process.
    """
    # Get new email here >> https://yopmail.com/en/email-generator
    test_email = "guxoppanave-7921@yopmail.com"
    test_password = constans.PASSWORD_LOGIN
    gender = 'MR'  # Choose MR or MRS
    page = MainPage(driver)
    page.open()
    main_page = page.open_sign_in_page()
    sign_in_page = main_page.user_create_account(test_email)
    registration_page = sign_in_page.create_new_user(test_email, test_password, gender)
    assert "Welcome to your account" in registration_page[0].text
