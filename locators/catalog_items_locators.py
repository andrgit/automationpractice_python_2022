from selenium.webdriver.common.by import By


class CatalogItemsLocators:
    WOMAN_ITEMS_LINK = (By.XPATH, "//*[@id='block_top_menu']/ul/li[1]/a")
    DRESSES_ITEM_LINK = (By.XPATH, "//*[@id='block_top_menu']/ul/li[2]/a")
    TSHIRTS_ITEM_LINK = (By.XPATH, "//*[@id='block_top_menu']/ul/li[3]/a")
    BASKET_BTN = (By.XPATH, "//*[@title='View my shopping cart']")
    FIRST_ITEMS_IN_WOMAN_ELEMENTS_2 = (By.XPATH, "#//*[@data-id-product='1']")
    BLUE_COLOR_DRESS_LOCATOR = (By.XPATH, "//a[@id='color_20']")
    # MORE_IN_CATALOG_WHERE_BLUE_DRESS = (By.CSS_SELECTOR, "a#color_20.color_pick")
    QUANTITY_PLUS_BUTTON = (By.XPATH, "//*[@class='icon-plus']")
    QUANTITY_MINUS_BUTTON = (By.XPATH, "//*[@class='icon-minus']")
    ALL_SIZE_DROP_DOWN_LIST = (By.XPATH, "//*[@id='group_1']")
    SIZE_M_IN_DROP_DOWN_LIST = (By.XPATH, "//*[@title='M']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='add_to_cart']/button/span")
    PRODUCT_SUCCESS_ADDED_CART = (By.CLASS_NAME, ".layer_cart_product > h2")  # or //*[@class="icon-ok"] #text
    PROCEED_TO_CHECKOUT_BUTTON_ITEM = (By.XPATH, "//*[@class='button-container']/a/span")
    PROCEED_TO_CHECKOUT_BUTTON_IN_CART_SUMMARY = (By.XPATH, "//*[@id='center_column']/p[2]/a[1]")
    PROCEED_TO_CHECKOUT_BUTTON_IN_CART_ADDRESS = (By.XPATH, "//*[@id='center_column']/form/p/button")
    CHECKBOX_I_AGREE_IN_CART_SHIPPING = (By.XPATH, "//*[@id='cgv']")
    PROCEED_TO_CHECKOUT_BUTTON_IN_CART_SHIPPING = (By.XPATH, "//*[@name='processCarrier']")
    PAY_BY_BANK_WIRE_BUTTON = (By.XPATH, "//*[@class='bankwire']")
    I_CONFIRM_MY_ORDER_BUTTON = (By.XPATH, "//*[@id='cart_navigation']/button/span")
    YOUR_ORDER_COMPLETE_TEXT = (By.XPATH, "//*[@class='cheque-indent']/strong")

# //*[contains(@class,'myclass') and contains(text(),'qwerty')]
# //*[@class='myclass' and contains(text(),'qwerty')]
# //*[@class='icon-ok' and contains(text(),'Product successfully added')]
# //*[contains(@class,'icon-ok') and contains(text(),'Product successfully added')]
# // *[ @ id = "layer_cart"] / div[1] / div[1] / h2 / text()
