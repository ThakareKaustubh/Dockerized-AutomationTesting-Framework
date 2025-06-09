from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
import allure
import pytest


@allure.feature("User Registration")
@allure.story("New User Signup Flow")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.flaky(reruns=2, reruns_delay=4)
def test_valid_user_registration(driver_setup, base_url, data_test):
    user_data = data_test["registration_data"]

    driver = driver_setup
    driver.get(base_url)
    registrationpage = RegistrationPage(driver)

    with allure.step("Verify Home page loaded"):
        loginpage = LoginPage(driver)
        assert loginpage.check_page_load(), "Home Page did not load"

    with allure.step("Navigate to login/signup page"):
        loginpage.goto_login_signup_page()
        assert loginpage.verify_new_user_signup(), "New user signup section not visible"

    with allure.step("Register new user"):
        loginpage.register_username(user_data["username"])
        loginpage.register_email(user_data["email"])
        loginpage.submit_registration()
        assert loginpage.verify_registration_submit_text(), "Registration submit failed"

    with allure.step("Fill and verify registration form"):
        registrationpage.select_title(user_data["title"])
        registrationpage.verify_name(user_data["username"])
        registrationpage.verify_email(user_data["email"])
        registrationpage.enter_pass(user_data["password"])
    with allure.step("Fill birthdate"):
        registrationpage.select_bdate(user_data["birthdate"]["day"],
                                      user_data["birthdate"]["month"],
                                      user_data["birthdate"]["year"])
        registrationpage.scroll_down()
    with allure.step("Selecting checkboxes"):
        registrationpage.select_checkboxes()

    with allure.step("Fill and verify address details"):
        registrationpage.enter_address_details(user_data["address"]["first_name"],
                                               user_data["address"]["last_name"],
                                               user_data["address"]["company"],
                                               user_data["address"]["address1"],
                                               user_data["address"]["address2"],
                                               user_data["address"]["country"],
                                               user_data["address"]["state"],
                                               user_data["address"]["city"],
                                               user_data["address"]["zipcode"],
                                               user_data["address"]["mobile_number"])
        registrationpage.scroll_down()
    registrationpage.submit_form()
    assert registrationpage.verify_account_created(), "Account creation failed"

    with allure.step("Verify logged-in username"):
        registrationpage.continue_post_reg()
        assert f"{user_data['username']}" == registrationpage.check_logged_in_user(), "Login username mismatch"

    with allure.step("Verify and delete new account"):
        registrationpage.delete_created_account()
        assert registrationpage.delete_account_confirmation(), "Account deletion failed"
