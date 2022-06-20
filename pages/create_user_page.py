import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import constans
from locators.login_page_locators import LoginPageLocators
from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select

from pages.login_page import LoginPage


class CreateUserPage(BasePage):
    def create_new_user(self, email, password, gender):
        if gender == "MR":
            mr_radiobutton = self.find_element(RegistrationPageLocators.MR_RADIOBUTTON_LOCATOR)
            mr_radiobutton.click()
        else:
            mrs_radiobutton = self.find_element(RegistrationPageLocators.MRS_RADIOBUTTON_LOCATOR).click()
            mrs_radiobutton.click()
        first_name = self.find_element(RegistrationPageLocators.FIRST_NAME_FIELD_LOCATOR)
        first_name.send_keys(constans.FIRSTNAME_LOGIN)
        last_name = self.find_element(RegistrationPageLocators.LAST_NAME_FIELD_LOCATOR)
        last_name.send_keys(constans.LASTNAME_LOGIN)
        password_field = self.find_element(RegistrationPageLocators.PASSWORD_FIELD_LOCATOR)
        password_field.send_keys(password)

        # Date of Birth
        days_of_birth_dropdown = Select(self.driver.find_element_by_xpath(
            RegistrationPageLocators.DAYS_OF_BIRTH_DROPDOWN_LOCATOR_SELECT))
        days_of_birth_dropdown.select_by_value("5")

        months_of_birth_drop_down = Select(self.driver.find_element_by_xpath(
            RegistrationPageLocators.MONTHS_OF_BIRTH_DROPDOWN_LOCATOR_SELECT))
        months_of_birth_drop_down.select_by_value("10")

        years_of_birth_drop_down = Select(self.driver.find_element_by_xpath(
            RegistrationPageLocators.YEARS_OF_BIRTH_DROPDOWN_LOCATOR_SELECT))
        years_of_birth_drop_down.select_by_value("1999")

        address = self.find_element(RegistrationPageLocators.ADDRESS_FIELD_LOCATOR)
        address.send_keys(constans.ADRESS_LOGIN)

        city = self.find_element(RegistrationPageLocators.CITY_FIELD_LOCATOR)
        city.send_keys(constans.CITY_LOGIN)

        state_drop_down = Select(self.driver.find_element_by_xpath(
            RegistrationPageLocators.STATE_DROPDOWN_LOCATOR_SELECT))
        time.sleep(2)
        state_drop_down.select_by_visible_text("California")

        zip_code = self.find_element(RegistrationPageLocators.ZIP_CODE_FIELD_LOCATOR)
        zip_code.send_keys(constans.ZIPCODE_LOGIN)

        mobile_phone = self.find_element(RegistrationPageLocators.MOBILE_PHONE_FIELD_LOCATOR)
        mobile_phone.send_keys(constans.MOBILE_PHONE_LOGIN)

        register_button = self.find_element(RegistrationPageLocators.REGISTER_BUTTON_LOCATOR)
        register_button.click()
        finish_registration = self.find_element(LoginPageLocators.WELCOME_TO_ACCOUNT_TEXT)
        return finish_registration, LoginPage(self.driver, self.driver.current_url)
