from selenium.webdriver.common.by import By


class LoginPageLocators:
    WOMAN_ITEMS_LINK = (By.XPATH, "//*[@id='block_top_menu']/ul/li[1]/a")
    DRESSES_ITEM_LINK = (By.XPATH, "//*[@id='block_top_menu']/ul/li[2]/a")
    TSHIRTS_ITEM_LINK = (By.XPATH, "//*[@id='block_top_menu']/ul/li[3]/a")
    BASKET_BTN = (By.XPATH, "//*[@title='View my shopping cart']")
    WELCOME_TO_ACCOUNT_TEXT = (By.XPATH, "//*[@class='info-account']")
    SEARCH_FIELD_LOCATOR = (By.XPATH, "//*[@id='search_query_top']")
    SEARCH_FIELD_BUTTON = (By.XPATH, "//*[@name='submit_search']")


