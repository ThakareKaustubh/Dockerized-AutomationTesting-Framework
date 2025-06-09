from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element_to_be_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        return  self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_text(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_urls(self, url_fragment):
        return self.wait.until(EC.url_contains(url_fragment))
