from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils
from utils.logger import get_logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver, timeout=10)
        self.home_page = (By.XPATH, "//a[normalize-space()='Home']")
        self.products_page = (By.XPATH, "//a[@href='/products']")
        self.cart_page = (By.XPATH, "//a[@href='/view_cart' and contains(., 'Cart')][1]")
        self.login_signup = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
        self.verify_logged_user = (By.XPATH, "//a[contains(text(), 'Logged in as')]/b")
        self.del_acc = (By.CSS_SELECTOR, "a[href='/delete_account']")
        self.del_cnf = (By.XPATH, "//b[contains(text(),'Account Deleted!')]")
        self.logout_btn = (By.XPATH, "//a[contains(., 'Logout')]")

    def goto_homepage(self):
        self.logger.info("Navigating to home page...")
        home = self.wait.wait_for_element_to_be_visible(self.home_page)
        home.click()
        self.logger.info("Successfully navigated to home page...")

    def goto_products_page(self):
        self.logger.info("Navigating to Products page...")
        products = self.wait.wait_for_element_to_be_visible(self.products_page)
        products.click()
        self.logger.info("Successfully navigated to products page...")

    def goto_cart_page(self):
        self.logger.info("Navigating to Cart page...")
        cart = self.wait.wait_for_element_to_be_visible(self.cart_page)
        cart.click()
        self.logger.info("Successfully navigated to cart page...")

    def goto_login_signup_page(self):
        self.logger.info("Navigating to Login / Signup page...")
        log_signin = self.wait.wait_for_element_to_be_visible(self.login_signup)
        log_signin.click()
        self.logger.info("Successfully navigated to login/signup page...")

    def scroll_to_element(self, element):
        self.logger.info(f"Scrolling to {element}...")
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    def scroll_until_visible(self, locator):
        element = self.wait.wait_for_element_to_be_visible(locator)
        self.scroll_to_element(element)
        return element

    def check_logged_in_user(self):
        self.logger.info("Checking the logged in user.")
        self.logger.info("Starting Username extraction")
        element = self.wait.wait_for_element_to_be_visible(self.verify_logged_user)
        return element.text

    def delete_created_account(self):
        self.logger.info("Deleting current account")
        del_account = self.wait.wait_for_element_to_be_clickable(self.del_acc)
        del_account.click()
        self.logger.info("Current account deleted.")

    def delete_account_confirmation(self):
        self.logger.info("Confirming account deleted")
        return self.wait.wait_for_element_to_be_visible(self.del_cnf).text == "ACCOUNT DELETED!"

    def click_logout_btn(self):
        self.logger.info("Clicking on the logout button.")
        self.wait.wait_for_element_to_be_clickable(self.logout_btn).click()
        self.logger.info("Clicked logout.")
