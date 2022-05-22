import allure
import pytest

import constans
from pages.main_page import MainPage


@allure.story("Create new user")
def test_create_new_user(driver):
    """
    The signup Process.
    """
    test_email = constans.EMAIL_NEW_LOGIN_FOR_REGISTRATION
    test_password = constans.PASSWORD_LOGIN
    gender = 'MR'  # MR or MRS
    page = MainPage(driver)
    page.open()
    main_page = page.open_sign_in_page()
    sign_in_page = main_page.user_create_account(test_email)
    registration_page = sign_in_page.create_new_user(test_email, test_password, gender)
    assert "Welcome to your account" in registration_page[0].text

    # assert #проверить зашли ли мы или нет

    # email_page = page.open_email_page(email_andrmy, password_andrmy)

    # last_send_message = email_page.open_last_send_message()

    # assert "mytestand1" in last_send_message.text, "We have a problem"

    #     email_andrmy = 'andrmytest1@gmail.com'
    #     password_andrmy = 'password123@'
    #     page = MainPage(driver)
    #     with allure.step('Open main page'):
    #         page.open()
    #     with allure.step('Open email page and send mail data'):
    #         email_page = page.open_email_page(email_andrmy, password_andrmy)
    #     with allure.step('Check In email page,the necessary email in the send messages'):
    #         last_send_message = email_page.open_last_send_message()
    #     assert "mytestand1" in last_send_message.text, "We have a problem"


# @allure.story("The Sign-in process for user - positive scenario")
# def test_login_user_positive(driver):
#     """
#     The Sign-in process
#       i. Positive scenario (Valid credentials)
#     """
#     email_test = constans.EMAIL_LOGIN
#     passw_test = constans.PASSWORD_LOGIN
#     page = MainPage(driver)
#     with allure.step('Open main page'):
#         page.open()
#     with allure.step('Open sign-in page'):
#         login_page = page.open_sign_in_page()
#     with allure.step('Try to login positive'):
#         sign_in_page = login_page.user_login(email_test, passw_test)
#     assert "Welcome to your account" in sign_in_page[0].text, "Problem with positive test"


# @allure.story("The Sign-in process for user - Negative scenario")
# def test_login_user_negative(driver):
#     """
#     The Sign-in process
#       ii. Negative scenario (Invalid credentials) and catch the error message
#     """
#     email_test = constans.EMAIL_LOGIN
#     passw_test = constans.PASSWORD_LOGIN_FAIL  # Wrong password
#     page = MainPage(driver)
#     with allure.step('Open main page'):
#         page.open()
#     with allure.step('Open sign-in page'):
#         login_page = page.open_sign_in_page()
#     with allure.step('Try to login negative scenario'):
#         sign_in_page = login_page.user_login(email_test, passw_test)
#     assert "Authentication failed" in sign_in_page[0].text


# @allure.story("Buy 2 summer dresses with params")
# def test_login_and_buy_2_summer_dress(driver):
#     # заходим в личный кабинет(логин пэйдж)
#     # нажать на поиск + отправить Printed Summer Dress
#     # Ищем на странице платье с синим цветом,и нажимаем на него
#     # Открываются данные платья, и там проверить синий ли выбран
#     # Нажать 2 шт, размер М и добавить в корзину платья
#
#     """
#     The "Printed Summer Dress" purchase process.
#         i. Define the Quantity as 2
#         ii. Select Medium (M) as Size
#         iii. Select Blue as color
#         iv. Pay by bank wire
#     """
#     email_test = constans.EMAIL_LOGIN
#     passw_test = constans.PASSWORD_LOGIN
#     page = MainPage(driver)
#     with allure.step('Open main page'):
#         page.open()
#     with allure.step('Open sign-in page'):
#         login_page = page.open_sign_in_page()
#     with allure.step('Try to login negative scenario'):
#         sign_in_page = login_page.user_login(email_test, passw_test)
#         add_item_cart = sign_in_page[1].add_dress_to_card_and_buy()
#     with allure.step('Check add and buy dress'):
#         assert "Your order on My Store is complete" in add_item_cart.text, "Problem with order"
