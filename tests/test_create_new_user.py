import allure

import constans
from pages.main_page import MainPage


@allure.story("Create new user")
def test_create_new_user(driver):
    """
    The process of creating a new user.
    """
    # Get new email here >> https://yopmail.com/en/email-generator
    test_email = "douquakouffatroi-7903@yopmail.com"
    test_password = constans.PASSWORD_LOGIN
    gender = 'MR'  # Choose MR or MRS
    # day.month.year
    date_of_birth = "5.10.1999"
    city_in_usa = "California"
    page = MainPage(driver)
    page.open()
    main_page = page.open_sign_in_page()
    sign_in_page = main_page.user_create_account(test_email)
    registration_page = sign_in_page.create_new_user(test_password,
                                                     gender, date_of_birth,
                                                     city_in_usa)
    assert "Welcome to your account" in registration_page[0].text
