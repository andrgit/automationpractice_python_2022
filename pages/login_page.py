import time

import constans
from locators.catalog_items_locators import CatalogItemsLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


# заходим в личный кабинет(логин пэйдж)
# нажать на поиск + отправить Printed Summer Dress
# Ищем на странице платье с синим цветом,и нажимаем на него
# Открываются данные платья, и там проверить синий ли выбран
# Нажать 2 шт, размер М и добавить в корзину платья

class LoginPage(BasePage):
    def try_to_add_item(self):
        search_field = self.find_element(LoginPageLocators.SEARCH_FIELD_LOCATOR)
        search_field.send_keys(constans.TEST_DRESSES)
        search_button = self.find_element(LoginPageLocators.SEARCH_FIELD_BUTTON)
        search_button.click()
        blue_dress = self.find_element(CatalogItemsLocators.BLUE_COLOR_DRESS_LOCATOR)
        blue_dress.click()  # не работает
        blue_dress.click()  # не работает
        time.sleep(5)
        quantity_plus_dress = self.find_element(CatalogItemsLocators.QUANTITY_PLUS_BUTTON)
        quantity_plus_dress.click()
        size_dress_drop_list = self.find_element(CatalogItemsLocators.ALL_SIZE_DROP_DOWN_LIST)
        size_dress_drop_list.click()
        choose_m_size_dress = self.find_element(CatalogItemsLocators.SIZE_M_IN_DROP_DOWN_LIST)
        choose_m_size_dress.click()
        add_to_card_dress = self.find_element(CatalogItemsLocators.ADD_TO_CART_BUTTON)
        add_to_card_dress.click()

        # proceed_to_checkout = self.find_element(CatalogItemsLocators.PROCEED_TO_CHECKOUT_BUTTON_ITEM)
        # proceed_to_checkout.click()
        # assert



        # email_field.send_keys(email)
        # passw_field = self.find_element(SignInPageLocators.PASSW_FIELD_LOG_IN)
        # passw_field.send_keys(passw)
        # sign_in_btn = self.find_element(SignInPageLocators.SIGN_IN_BTN_LOGIN)
        # sign_in_btn.click()
        # sign_in_success = self.find_element(LoginPageLocators.WELCOME_TO_ACCOUNT_TEXT)
        # if sign_in_success:
        #     return sign_in_success, LoginPage(self.driver, self.driver.current_url)
        # else:
        #     sign_in_failed = self.find_element(SignInPageLocators.FAIL_LOGIN_MESSG)
        #     return sign_in_failed, LoginPage(self.driver, self.driver.current_url)

    def try_to_remove_item(self):
        pass
