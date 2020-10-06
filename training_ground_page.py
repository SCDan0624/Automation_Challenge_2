from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage


class TrainingGroundPage(BasePage):

    url = 'https://techstepacademy.com/training-ground/'

    @property
    def button1(self):
        locator = (By.ID, 'b1')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )

# Note our custom BaseElement object always has
# self.locator = (self.by, self.value) which is why by = locator[0]
# and why value = locator[1]
