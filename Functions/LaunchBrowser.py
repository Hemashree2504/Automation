import os

from selenium import webdriver

from Functions.Pages import Pages


class LaunchBrowser(Pages):
    driver = None

    def __init__(self):
        Pages.__init__(self)
        self.ChromeDriverPath = None
        self.FirefoxDriverPath = None

    def launch_browser(self, browser_name):
        driver_path = os.getcwd()
        if browser_name == 'Chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            self.ChromeDriverPath = driver_path + "/Functions/WinDriver/chromedriver"
            self.driver = webdriver.Chrome(executable_path=self.ChromeDriverPath, options=chrome_options)
            self.driver.implicitly_wait(5)
        else:
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--start-maximized")
            self.FirefoxDriverPath = driver_path + "/Functions/WinDriver/geckodriver"
            self.driver = webdriver.Chrome(executable_path=self.FirefoxDriverPath, options=firefox_options)
            self.driver.implicitly_wait(5)

        return self.driver
