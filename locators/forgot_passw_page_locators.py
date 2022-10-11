from selenium.webdriver.common.by import By


class ForgotPasswPageLocators:
    email_field = (By.XPATH, "//*[@id='email']")
    retrieve_password_btn = (By.CSS_SELECTOR, "button.btn:nth-child(1)")
    back_to_login_btn = (By.XPATH, "a[title='Back to Login']")
    confirm_message = (By.CSS_SELECTOR, "p.alert.alert-success")
