import time

import constans
from locators.catalog_items_locators import CatalogItemsLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# заходим в личный кабинет(логин пэйдж)
# нажать на поиск + отправить Printed Summer Dress
# Ищем на странице платье с синим цветом,и нажимаем на него
# Открываются данные платья, и там проверить синий ли выбран
# Нажать 2 шт, размер М и добавить в корзину платья

class LoginPage(BasePage):
    SEARCH_FIELD = (By.XPATH, "//*[@id='search_query_top']")
    SEARCH_FIELD_BUTTON = (By.XPATH, "//*[@name='submit_search']")

    def click_to_search_field(self, value):
        search_field = self.find_element(self.SEARCH_FIELD)
        search_field.send_keys(value)

    def click_search_button(self):
        search_button = self.find_element(self.SEARCH_FIELD_BUTTON)
        search_button.click()

    def add_dress_to_card_and_buy(self):
        search_field = self.find_element(
            LoginPageLocators.SEARCH_FIELD_LOCATOR)
        search_field.send_keys(constans.TEST_DRESSES)
        search_button = self.find_element(
            LoginPageLocators.SEARCH_FIELD_BUTTON)
        search_button.click()
        blue_dress = self.find_element(
            CatalogItemsLocators.BLUE_COLOR_DRESS_LOCATOR)
        blue_dress.click()
        blue_dress.click()
        quantity_plus_dress = self.find_element(
            CatalogItemsLocators.QUANTITY_PLUS_BUTTON)
        quantity_plus_dress.click()
        size_dress_drop_list = self.find_element(
            CatalogItemsLocators.ALL_SIZE_DROP_DOWN_LIST)
        size_dress_drop_list.click()
        choose_m_size_dress = self.find_element(
            CatalogItemsLocators.SIZE_M_IN_DROP_DOWN_LIST)
        choose_m_size_dress.click()
        add_to_card_dress = self.find_element(
            CatalogItemsLocators.ADD_TO_CART_BUTTON)
        add_to_card_dress.click()
        push_proceed_to_checkout = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                CatalogItemsLocators.PROCEED_TO_CHECKOUT_BUTTON_ITEM))
        push_proceed_to_checkout.click()
        push_proceed_to_checkout_summary = self.find_element(
            CatalogItemsLocators.PROCEED_TO_CHECKOUT_BUTTON_IN_CART_SUMMARY)
        push_proceed_to_checkout_summary.click()
        push_proceed_to_checkout_address = self.find_element(
            CatalogItemsLocators.PROCEED_TO_CHECKOUT_BUTTON_IN_CART_ADDRESS)
        push_proceed_to_checkout_address.click()
        checkbox_i_agree_terms_shipping = self.find_element(
            CatalogItemsLocators.CHECKBOX_I_AGREE_IN_CART_SHIPPING)
        checkbox_i_agree_terms_shipping.click()
        push_proceed_to_checkout_shipping = self.find_element(
            CatalogItemsLocators.PROCEED_TO_CHECKOUT_BUTTON_IN_CART_SHIPPING)
        push_proceed_to_checkout_shipping.click()
        pay_by_bank_order = self.find_element(
            CatalogItemsLocators.PAY_BY_BANK_WIRE_BUTTON)
        pay_by_bank_order.click()
        confirm_order_button = self.find_element(
            CatalogItemsLocators.I_CONFIRM_MY_ORDER_BUTTON)
        confirm_order_button.click()
        order_complete = self.find_element(
            CatalogItemsLocators.YOUR_ORDER_COMPLETE_TEXT)
        return order_complete
        # return order_complete, LoginPage(self.driver, self.driver.current_url)
