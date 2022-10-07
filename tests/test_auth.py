# import allure
#
# def test_auth_positive(auth_page):
#     auth_page.click_to_login_field('login')
#     auth_page.click_to_password_field('password')
#     auth_page.click_submit_button()
#
#
# @allure.title('Авторизация пользователя')
# def test_auth_negative(site):
#     site.auth_page.click_to_login_field('login')
#     site.auth_page.click_to_password_field('password')
#     site.auth_page.click_submit_button()
#     site.simple_page.click_to_password_field()
#     assert site.simple_page
#
#
# def test_auth_negative_short(site):
#     site.auth_page.login_user('login', 'password')
#     site.simple_page.click_to_password_field()
#
#
# @allure.title('Переход на SimplePage после авторизации')
# def test_auth_negative_with_auth(site_w_login):
#     site_w_login.simple_page.click_to_password_field()