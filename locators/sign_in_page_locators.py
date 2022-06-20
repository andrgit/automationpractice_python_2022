from selenium.webdriver.common.by import By


class SignInPageLocators:
    EMAIL_FIELD_CREATE_ACCOUNT = (By.XPATH, "//*[@id='email_create']")
    CREATE_AN_ACCOUNT_BTN = (By.XPATH, "//*[@id='SubmitCreate']")
    EMAIL_FIELD_LOG_IN = (By.XPATH, "//*[@id='email']")
    PASSW_FIELD_LOG_IN = (By.XPATH, "//*[@id='passwd']")
    FORGOT_YOUR_PASSW_LINK = (By.XPATH, "//*[@id='login_form']/div/p[1]/a")
    SIGN_IN_BTN_LOGIN = (By.XPATH, "//*[@id='SubmitLogin']")
    FAIL_LOGIN_MESSG = (By.XPATH, "//*[@id='center_column']/div[1]")
    ERROR_LOGIN_REGISTERED = (By.XPATH, "//*[@id='create_account_error']//li")
