import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class WebDriverHelper:
    def __init__(self):
        pass

    def find_element(self, locator, value, wait_time):

        if wait_time:
            wait = WebDriverWait(self.driver, wait_time)
        else:
            wait = WebDriverWait(self.driver, 30)

        try:
            if locator == 'xpath':
                element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, value)))
            elif locator == 'id':
                element = wait.until(expected_conditions.visibility_of_element_located((By.ID, value)))
            elif locator == 'css':
                element = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, value)))
            elif locator == 'classname':
                element = wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, value)))
            elif locator == 'tagname':
                element = wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, value)))
            elif locator == 'linktext':
                element = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, value)))
            elif locator == 'partiallinktext':
                element = wait.until(expected_conditions.visibility_of_element_located((By.PARTIAL_LINK_TEXT, value)))
            elif locator == 'name':
                element = wait.until(expected_conditions.visibility_of_element_located((By.NAME, value)))


        except Exception as e:
            pytest.fail(msg=str(e))
            self.driver.quit()

        return element

    def go_to_url(self, url):

        self.driver.get(url)

    def click(self, element):
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def get_elements_by_xpath(self, element_xpath):
        return self.driver.find_elements_by_xpath(element_xpath)

    def switch_to_window(self, window_no):

        window = self.driver.window_handles
        self.driver.switch_to.window(window[window_no])

    def refresh(self):
        self.driver.get(self.driver.current_url)

    def execute_script(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def move_to_element(self,element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
