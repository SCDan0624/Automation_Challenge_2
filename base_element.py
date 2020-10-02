from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by

        self.web_element = None

    def find(self):
        # Must be in this order: by, then value
        locator = (self.by, self.value)
        element = WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located(locator=locator))
        self.web_element = element
        return None

        # By is a class that has attributes such as ID = 'id', XPATH = 'xpath'
