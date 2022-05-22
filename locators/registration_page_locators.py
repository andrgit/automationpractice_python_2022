from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    MR_RADIOBUTTON_LOCATOR = (By.XPATH, "//*[@id='id_gender1']")
    MRS_RADIOBUTTON_LOCATOR = (By.XPATH, "//*[@id='id_gender2']")
    FIRST_NAME_FIELD_LOCATOR = (By.XPATH, "//*[@id='customer_firstname']")
    LAST_NAME_FIELD_LOCATOR = (By.XPATH, "//*[@id='customer_lastname']")
    EMAIL_FIELD_LOCATOR = (By.XPATH, "//*[@id='email']")
    PASSWORD_FIELD_LOCATOR = (By.XPATH, "//*[@id='passwd']")

    DAYS_OF_BIRTH_DROPDOWN_LOCATOR_SELECT = "//*/select[@id='days']"
    # DAYS_OF_BIRTH_DROPDOWN_LOCATOR = (By.XPATH, "//*[@id='days']")

    MONTHS_OF_BIRTH_DROPDOWN_LOCATOR_SELECT = "//*/select[@id='months']"
    # MONTHS_OF_BIRTH_DROPDOWN_LOCATOR = (By.XPATH, "//*[@id='months']")

    YEARS_OF_BIRTH_DROPDOWN_LOCATOR_SELECT = "//*/select[@id='years']"
    # YEARS_OF_BIRTH_DROPDOWN_LOCATOR = (By.XPATH, "//*[@id='years']")

    ADDRESS_FIELD_LOCATOR = (By.XPATH, "//*[@id='address1']")
    CITY_FIELD_LOCATOR = (By.XPATH, "//*[@id='city']")

    # STATE_DROPDOWN_LOCATOR = (By.XPATH, "//*[@id='id_state']")
    STATE_DROPDOWN_LOCATOR_SELECT = "//*/select[@id='id_state']"

    ZIP_CODE_FIELD_LOCATOR = (By.XPATH, "//*[@id='postcode']")
    MOBILE_PHONE_FIELD_LOCATOR = (By.XPATH, "//*[@id='phone_mobile']")
    REGISTER_BUTTON_LOCATOR = (By.XPATH, "//*[@id='submitAccount']")
