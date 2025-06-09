from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome", headless=False):
        if browser_name.lower() == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920x1080")  # Ensure elements are visible
                options.add_argument("--disable-popup-blocking")  # Disable popup blocking
                options.add_argument("--no-sandbox")  # Bypass OS security (useful in Docker)
                options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
                options.add_argument("--use-angle=default")
                options.add_argument("--start-maximised")
                options.add_argument("--enable-logging")
                options.add_argument("--no-user-data-dir")
                options.add_argument("--v=1") 
            return webdriver.Chrome(options=options)

        elif browser_name.lower() == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")
            return webdriver.Firefox(options=options)

        else:
            raise Exception(f"Browser '{browser_name}' is not supported.")
