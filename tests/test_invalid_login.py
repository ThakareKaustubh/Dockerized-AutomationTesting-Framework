import allure
from pages.login_page import LoginPage


@allure.feature("User Login")
@allure.story("Invalid User login Flow")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_using_invalid_credentials(driver_setup, base_url):
    driver = driver_setup
    driver.get(base_url)

    with allure.step("Verify Home page loaded"):
        loginpage = LoginPage(driver)
        assert loginpage.check_page_load(), "Home Page did not load"

    with allure.step("Navigate to login/signup page"):
        loginpage.goto_login_signup_page()
        assert loginpage.verify_login_to_acc_is_visible(), "Login to your account not visible"

    with allure.step("Entering invalid credentials"):
        invalid_email, invalid_password = loginpage.get_invalid_creds()
        loginpage.enter_username(invalid_email)
        loginpage.enter_password(invalid_password)
        loginpage.submit_login()

    with allure.step("Verify invalid login message"):
        assert loginpage.verify_invalid_login(), "Your email or password is incorrect!"
