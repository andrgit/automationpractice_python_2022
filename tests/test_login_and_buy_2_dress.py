import allure

import constans
from pages.main_page import MainPage


@allure.story("Buy 2 summer dresses with params")
def test_login_and_buy_2_summer_dress(driver):
    # заходим в личный кабинет(логин пэйдж)
    # нажать на поиск + отправить Printed Summer Dress
    # Ищем на странице платье с синим цветом,и нажимаем на него
    # Открываются данные платья, и там проверить синий ли выбран
    # Нажать 2 шт, размер М и добавить в корзину платья

    """
    The "Printed Summer Dress" purchase process.
        i. Define the Quantity as 2
        ii. Select Medium (M) as Size
        iii. Select Blue as color
        iv. Pay by bank wire
    """

    email_test = "ciprexullagri-3473@yopmail.com"
    passw_test = constans.PASSWORD_LOGIN
    page = MainPage(driver)
    with allure.step('Open main page'):
        page.open()
    with allure.step('Open sign-in page'):
        login_page = page.open_sign_in_page()
    with allure.step('Try to login negative scenario'):
        sign_in_page = login_page.user_login(email_test, passw_test)
        add_item_cart = sign_in_page[1].add_dress_to_card_and_buy()
    with allure.step('Check add and buy dress'):
        assert "Your order on My Store is complete" in add_item_cart.text, \
            "Problem with order"
