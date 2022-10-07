import pytest
from selenium import webdriver


# from pages.auth_page import AuthPage
# from pages.main_page import MainPage
# from pages.simple_page import Site


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
#
#
# @pytest.fixture()
# def auth_page(driver):
#     page = AuthPage(driver)
#     return page
#
#
# @pytest.fixture()
# def main_page(driver):
#     page = MainPage(driver)
#     return page
#
#
# @pytest.fixture()
# def profile_page(driver):
#     page = AuthPage(driver)
#     return page
#
#
# @pytest.fixture()
# def site(driver):
#     site = Site(driver)
#     return site
#
#
# @pytest.fixture()
# def site_w_login(driver):
#     site = Site(driver)
#     site.auth_page.login_user('login', 'password')
#     return site
