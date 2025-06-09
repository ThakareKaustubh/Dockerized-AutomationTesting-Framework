from pages.base_page import BasePage
from utils.wait_utils import WaitUtils
from utils.logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver, timeout=10)
        self.radio_id1 = (By.ID, "id_gender1")
        self.radio_id2 = (By.ID, "id_gender2")
        self.reg_name = (By.XPATH, "//*[@id='name']")
        self.reg_email = (By.XPATH, "//*[@id='email']")
        self.reg_pass = (By.XPATH, "//*[@id='password']")
        self.days = (By.XPATH, "//*[@id='days']")
        self.months = (By.XPATH, "//*[@id='months']")
        self.years = (By.XPATH, "//*[@id='years']")
        self.chk_box1 = (By.XPATH, "//*[@id='newsletter']")
        self.chk_box2 = (By.XPATH, "//*[@id='optin']")
        self.first_name = (By.XPATH, "//*[@id='first_name']")
        self.last_name = (By.XPATH, "//*[@id='last_name']")
        self.company = (By.XPATH, "//*[@id='company']")
        self.address1 = (By.XPATH, "//*[@id='address1']")
        self.address2 = (By.XPATH, "//*[@id='address2']")
        self.country = (By.XPATH, "//*[@id='country']")
        self.state = (By.XPATH, "//*[@id='state']")
        self.city = (By.XPATH, "//*[@id='city']")
        self.zip_code = (By.XPATH, "//*[@id='zipcode']")
        self.mobile_num = (By.XPATH, "//*[@id='mobile_number']")
        self.submit = (By.XPATH, "//button[@data-qa='create-account']")
        self.verify_complete = (By.XPATH, "//b[text()='Account Created!']")
        self.continue_btn = (By.XPATH, "//a[@data-qa='continue-button']")

    def select_title(self, title):
        self.logger.info("Selecting title (gender).")
        if title == "Mr":
            self.wait.wait_for_element_to_be_clickable(self.radio_id1).click()
        elif title == "Mrs":
            self.wait.wait_for_element_to_be_clickable(self.radio_id2).click()
        self.logger.info("Title selected.")

    def verify_name(self, name):
        self.logger.info(f"Verifying name field pre-filled with: {name}")
        val = self.wait.wait_for_element_to_be_visible(self.reg_name).get_attribute("value")
        return val == name

    def verify_email(self, email):
        self.logger.info(f"Verifying email field pre-filled with: {email}")
        val = self.wait.wait_for_element_to_be_visible(self.reg_email).get_attribute("value")
        return val == email

    def enter_pass(self, password):
        self.logger.info("Entering password.")
        pass_field = self.wait.wait_for_element_to_be_visible(self.reg_pass)
        pass_field.clear()
        pass_field.send_keys(password)

    def select_bdate(self, day, month, year):
        self.logger.info(f"Selecting birth date: Day={day}, Month={month}, Year={year}")
        Select(self.wait.wait_for_element_presence(self.days)).select_by_value(day)
        Select(self.wait.wait_for_element_presence(self.months)).select_by_value(month)
        Select(self.wait.wait_for_element_presence(self.years)).select_by_value(year)

    def select_checkboxes(self):
        self.logger.info("Selecting checkboxes for newsletter and special offers.")
        self.wait.wait_for_element_to_be_clickable(self.chk_box1).click()
        self.wait.wait_for_element_to_be_clickable(self.chk_box2).click()
        self.logger.info("Selecting checkboxes complete.")

    def enter_address_details(self, fname, lname, company, address1, address2, country_name, state_name, city_name, zip,
                              mob_number):
        self.logger.info("Filling address details.")
        self.wait.wait_for_element_to_be_visible(self.first_name).send_keys(fname)
        self.wait.wait_for_element_to_be_visible(self.last_name).send_keys(lname)
        self.wait.wait_for_element_to_be_visible(self.company).send_keys(company)
        self.wait.wait_for_element_to_be_visible(self.address1).send_keys(address1)
        self.wait.wait_for_element_to_be_visible(self.address2).send_keys(address2)
        Select(self.wait.wait_for_element_to_be_clickable(self.country)).select_by_value(country_name)
        self.wait.wait_for_element_to_be_visible(self.state).send_keys(state_name)
        self.wait.wait_for_element_to_be_visible(self.city).send_keys(city_name)
        self.wait.wait_for_element_to_be_visible(self.zip_code).send_keys(zip)
        self.wait.wait_for_element_to_be_visible(self.mobile_num).send_keys(mob_number)
        self.logger.info("Address details filled")

    def submit_form(self):
        self.logger.info("Submitting the registration form.")
        self.wait.wait_for_element_to_be_clickable(self.submit).click()
        self.logger.info("Registration from submission complete.")

    def verify_account_created(self):
        self.logger.info("Verifying 'Account Created!' confirmation.")
        return self.wait.wait_for_element_to_be_visible(self.verify_complete).text == 'ACCOUNT CREATED!'

    def continue_post_reg(self):
        self.logger.info("Clicking continue post successfully account creation.")
        return self.wait.wait_for_element_to_be_clickable(self.continue_btn).click()

    def scroll_down(self, pixels=500):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
