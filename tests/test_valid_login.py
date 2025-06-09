import allure
from pages.login_page import LoginPage
from utils.create_user_api import create_user_from_api
import pytest


@allure.feature("User Login")
@allure.story("Valid User login Flow")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.flaky(reruns=2, reruns_delay=4)
def test_login_using_valid_credentials(driver_setup, base_url):
    valid_email, valid_password, valid_username = create_user_from_api(base_url)
    driver = driver_setup
    driver.get(base_url)

    with allure.step("Verify Home page loaded"):
        loginpage = LoginPage(driver)
        assert loginpage.check_page_load(), "Home Page did not load"

    with allure.step("Navigate to login/signup page"):
        loginpage.goto_login_signup_page()
        assert loginpage.verify_login_to_acc_is_visible(), "Login to your account not visible"

    with allure.step("Entering valid credentials"):
        loginpage.enter_username(valid_email)
        loginpage.enter_password(valid_password)
        loginpage.submit_login()

    with allure.step("Verify logged-in username"):
        assert valid_username == loginpage.check_logged_in_user(), "Login username mismatch"

    with allure.step("Verify and delete account"):
        loginpage.delete_created_account()
        assert loginpage.delete_account_confirmation(), "Account deletion failed"
