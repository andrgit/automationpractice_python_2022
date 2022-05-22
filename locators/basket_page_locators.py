from selenium.webdriver.common.by import By


class BasketPageLocators:
    DELETE_ITEMS_BTN = (By.CLASS_NAME, "i.icon-trash")
    WARNING_BASKET_EMPTY = (By.CLASS_NAME, "p.alert.alert-warning")
