import allure

import constans
from pages.main_page import MainPage


@allure.story("Create new user with already created email negative")
def test_create_new_user_with_created_email_negative(driver):
    """
    Negative test with already created email in the site.
    """
    test_email = constans.EMAIL_LOGIN
    page = MainPage(driver)
    page.open()
    main_page = page.open_sign_in_page()
    sign_in_page = main_page.user_create_account(test_email)
    assert "email address has already been registered." \
           in sign_in_page[0].text
